const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
let inputPtr = 0;
const input = () => lines[inputPtr++];
