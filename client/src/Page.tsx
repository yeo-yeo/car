import { sendMove } from 'helpers/sendMove';
import React from 'react';

export const Page = () => {
    return (
        <div
            style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                height: '90vh',
            }}
        >
            <div
                style={{
                    display: 'grid',
                    gridTemplateColumns: '1fr 1fr 1fr',
                    gridGap: '10px',
                    justifyContent: 'center',
                    alignItems: 'center',
                    height: '150px',
                    width: '150px',
                    textAlign: 'center',
                }}
                className="grid"
            >
                <div></div>
                <div>
                    {' '}
                    <button onClick={() => sendMove('F')}>F</button>
                </div>
                <div></div>
                <div>
                    <button onClick={() => sendMove('L')}>L</button>
                </div>
                <div></div>
                <div>
                    <button onClick={() => sendMove('R')}>R</button>
                </div>
                <div></div>
                <div>
                    {' '}
                    <button onClick={() => sendMove('B')}>B</button>
                </div>
                <div></div>
            </div>

            <button onClick={() => sendMove('S')} style={{ marginTop: '64px' }}>
                Stop
            </button>
        </div>
    );
};
