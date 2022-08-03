#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
fs.writeFileSync(argv[4], fs.readFileSync(argv[2], 'utf-8') + fs.readFileSync(argv[3], 'utf-8'));
