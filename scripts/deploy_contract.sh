#!/bin/bash
# This is a helper script for building and deploying the smart contract

# Build the Solana smart contract
anchor build

# Deploy the smart contract to the Solana blockchain
anchor deploy
