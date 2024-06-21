type move = 'F' | 'B' | 'L' | 'R' | 'S';

export const sendMove = (move: move) => {
    const url =
        window.location.href.includes('local') ||
        window.location.href.includes('127')
            ? 'http://localhost:3000/move'
            : 'https://car.rcdis.co/move';

    fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: move }),
    }).catch((e) => console.error(e));
};
