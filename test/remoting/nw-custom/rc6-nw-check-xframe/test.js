var http = require('http').createServer(function (req, res) {
  res.writeHead(200, {'X-Frame-Options': 'DENY'});
  res.end('Hello World!');
}).listen(3000)
setTimeout(function() {
  ifabc = document.getElementById("abc");
  ifabc.src = "http://127.0.0.1:3000/"
  // ifabc.onload = function() {
	 //  assert.equal(ifabc.contentWindow.location.href,"about:blank");
	 //  done();
  // }
},200);