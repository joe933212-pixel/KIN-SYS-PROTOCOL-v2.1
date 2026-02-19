import React from 'react';
import { useEffect, useState } from 'react';
import Web3 from 'web3';

const App: React.FC = () => {
    const [account, setAccount] = useState<string | null>(null);
    const [balance, setBalance] = useState<string>('0');
    const [loading, setLoading] = useState<boolean>(true);

    // Initialize Web3 for Polygon network
    const web3 = new Web3(new Web3.providers.HttpProvider('https://polygon-rpc.com/'));

    // Connect to wallet
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]);
                loadBalance(accounts[0]);
            } catch (error) {
                console.error('Wallet connection failed:', error);
            }
        } else {
            alert('Please install MetaMask to use this app.');
        }
    };

    // Load balance of connected account
    const loadBalance = async (account: string) => {
        const weiBalance = await web3.eth.getBalance(account);
        setBalance(web3.utils.fromWei(weiBalance, 'ether'));
        setLoading(false);
    };

    useEffect(() => {
        if (account) loadBalance(account);
    }, [account]);

    return (
        <div>
            <h1>Dashboard</h1>
            <button onClick={connectWallet}>Connect Wallet</button>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <div>
                    <p>Account: {account}</p>
                    <p>Balance: {balance} ETH</p>
                </div>
            )}
        </div>
    );
};

export default App;