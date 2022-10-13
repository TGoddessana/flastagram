var express = require("express");

var path = require("path");
var app = express();

app.use(express.static(path.join(__dirname, "..")));
app.listen(3000);

app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "..", "post_list.html"));
});
