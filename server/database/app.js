const express = require('express');
const app = express();
const port = 3030;

app.get('/', function(req, res) {
    res.send("Welcome to the API");
});

app.listen(port, function() {
    console.log("Server running");
});