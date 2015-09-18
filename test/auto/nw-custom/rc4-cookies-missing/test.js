var ws = require('websocket.io')
  , http = require('http').createServer(function (req, res) {
    require('fs').createReadStream('./response.html').pipe(res);
  }).listen(3000)
  , server = ws.attach(http);

server.on('connection', function (socket) {
  socket.on('message', function (msg) {
    var cookies = socket.req.headers.cookie;
    if (cookies == 'test=1')
       process.exit(0);
  });
  socket.on('error', function (err) {
    console.log(err);
  });
});
  
window.open("http://127.0.0.1:3000");



