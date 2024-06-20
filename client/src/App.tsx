import React from 'react';
import { Page } from 'Page';
import { WebsocketsProvider } from 'WebsocketsContext';
import { IdentityProvider } from 'IdentityContext';

export const App = () => {
    return (
        <>
            {/* <IdentityProvider>
                <WebsocketsProvider
                    setInitialCanvasContent={setInitialCanvasContent}
                > */}
            <Page />
            {/* </WebsocketsProvider>
            </IdentityProvider> */}
        </>
    );
};
