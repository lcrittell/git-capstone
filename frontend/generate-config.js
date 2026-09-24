const fs = require("fs");

const apiUrl = process.env.API_URL;

if (!apiUrl) {
    throw new Error("API_URL environment variable is not set");
}

fs.writeFileSync(
    "frontend/js/config.js",
    `window.API_URL = "${apiUrl}";\n`
);

console.log("Generated frontend/js/config.js");