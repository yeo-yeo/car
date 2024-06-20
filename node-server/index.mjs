#!/usr/bin/env node

import fastify from "fastify";

const app = fastify();

// set of all the connections, to broadcast to (in practice i'm only expecting one))
const connectionReplies = new Set();

app.get("/sse", (request, reply) => {
  reply.hijack();
  reply.header("Content-Type", "text/event-stream");
  console.log("Opening SSE connection");

  connectionReplies.add(reply.raw);

  request.raw.on("close", () => {
    console.log("closing connection");
    connectionReplies.delete(request.raw);
  });
});

const allowedMoves = ["F", "B", "R", "L", "S"];

app.post("/move", (request, reply) => {
  console.log("Incoming move:", request.body);
  const { data } = request.body;

  if (allowedMoves.includes(allowedMoves)) {
    connectionReplies.forEach((r) => {
      console.log("Forwarding a message to a listening connection");
      r.write(`data:${data}\n`);
    });
  }

  reply.send("ok");
});

const start = async () => {
  try {
    await app.listen({ port: 3000 });
    console.log("Server started on port 3000");
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
};

start();
