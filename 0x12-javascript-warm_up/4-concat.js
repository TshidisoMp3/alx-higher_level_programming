#!/usr/bin/node

const args = process.argv;
let i = 2;

if (args.length === 2) {
  console.log("No argument");
}
if (args.length === 3) {
  console.log("Argument found");
}
if (args.length > 3) {
  console.log("Arguments found");
}

for (i; i < args.length; i++) {
  console.log(args[i]);
}
