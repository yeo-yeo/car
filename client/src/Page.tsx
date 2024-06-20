import React from 'react';

export const Page = () => {
    return (
        <>
            <button
                onClick={() => {
                    fetch(`http://localhost:3000/move`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ data: 'F' }),
                    })
                        .then(console.log)
                        .catch((e) => console.error(e));
                }}
            >
                F
            </button>
            <button
                onClick={() => {
                    fetch(`http://localhost:3000/move`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ data: 'B' }),
                    })
                        .then(console.log)
                        .catch((e) => console.error(e));
                }}
            >
                B
            </button>
        </>
    );
};
