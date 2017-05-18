//process.argv 控制台全局变量数组
//var net = require('net');
var http = require('http');
var url = require('url');
// var fs = require('fs');
// var map = require('through2-map');
// var server = net.createServer(function(socket) {
//     socket.write(now() + '\n');
//     socket.end();
// });
// server.listen(process.argv[2]);

// function now() {
//     var d = new Date();
//     return d.getFullYear() + '-' +
//         zeroFill(d.getMonth() + 1) + '-' +
//         zeroFill(d.getDate()) + ' ' +
//         zeroFill(d.getHours()) + ':' +
//         zeroFill(d.getMinutes());
// }

// function zeroFill(i) {
//     return (i < 10 ? "0" : "") + i;
// }
// var server = http.createServer(function(req,res){
//     if(req.method.toUpperCase() == 'POST'){
//     req.pipe(map(function (chunk) {
//         return chunk.toString().toUpperCase();
//       })).pipe(res);
//     }
// });
// server.listen(process.argv[2]);

    function parsetime (time) {
      return {
        hour: time.getHours(),
        minute: time.getMinutes(),
        second: time.getSeconds()
      }
    }

    function unixtime (time) {
      return { unixtime: time.getTime() }
    }

    var server = http.createServer(function (req, res) {
      var parsedUrl = url.parse(req.url, true)
      var time = new Date(parsedUrl.query.iso)
      var result

      if (/^\/api\/parsetime/.test(req.url)) {
        result = parsetime(time)
      } else if (/^\/api\/unixtime/.test(req.url)) {
        result = unixtime(time)
      }

      if (result) {
        res.writeHead(200, { 'Content-Type': 'application/json' })
        res.end(JSON.stringify(result))
      } else {
        res.writeHead(404)
        res.end()
      }
    })
    server.listen(Number(process.argv[2]))
     
