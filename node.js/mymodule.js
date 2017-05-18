var fs = require('fs');
var path = require('path');

module.exports = function(filePath,fileExtension,callback){
fs.readdir(filePath, function(err,data){
    if(err)
        return callback(err);
    var arr = [];
    data.forEach(function(file){
        if(path.extname(file) === '.' + fileExtension){
            arr.push(file);
        }
    });
    callback(null,arr);
});
};
