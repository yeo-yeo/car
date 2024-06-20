#!/usr/bin/env node

import fastify from "fastify";
import cors from "@fastify/cors";
import fastifyStatic from "@fastify/static";
import { IncomingMessage, ServerResponse } from "http";
import path from "path";

const staticDirectory = path.join(__dirname, "..", "..", "client", "public");

const start = async () => {
  try {
    const app = fastify();

    await app.register(cors, {
      origin: "*",
    });

    app.register(fastifyStatic, {
      root: staticDirectory,
      prefix: "/",
    });

    app.get("/", (request, reply) => {
      reply.sendFile("index.html");
    });

    // set of all the connections, to broadcast to (in practice i'm only expecting one))
    const connectionReplies: Set<ServerResponse<IncomingMessage>> = new Set();

    app.get("/sse", (request, reply) => {
      // reply.hijack();
      const headers = {
        "Content-Type": "text/event-stream",
        Connection: "keep-alive",
        "Cache-Control": "no-cache",
      };
      reply.raw.writeHead(200, headers);
      reply.raw.write("data:connected");

      console.log("Opening SSE connection");

      connectionReplies.add(reply.raw);

      request.raw.on("close", () => {
        console.log("closing connection");
        connectionReplies.delete(reply.raw);
      });
    });

    const allowedMoves = ["F", "B", "R", "L", "S"];

    app.post("/move", (request, reply) => {
      console.log("Incoming move:", request.body);

      if (
        !request.body ||
        typeof request.body !== "object" ||
        !("data" in request.body) ||
        typeof request.body.data !== "string"
      ) {
        reply.send(
          "error - bad input format. expect json obj in form {data: string}"
        );
        return;
      }

      const { data } = request.body;

      if (!allowedMoves.includes(data)) {
        reply.send("error - move not supported");
        return;
      }

      connectionReplies.forEach((r) => {
        console.log("Forwarding a message to a listening connection");
        r.write(`data:${data}\n`);
      });

      reply.send("ok");
    });

    await app.listen({ port: 3000 });
    console.log("Server started on port 3000");
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
};

start().catch(console.error);
