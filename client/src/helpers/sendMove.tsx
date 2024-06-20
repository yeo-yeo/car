type move = 'F' | 'B' | 'L' | 'R' | 'S';

export const sendMove = (move: move) => {
    fetch(`http://localhost:3000/move`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: move }),
    }).catch((e) => console.error(e));
};
