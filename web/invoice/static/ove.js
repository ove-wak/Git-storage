//$SCRIPT_ROOT = {{request.script_root|tojson|safe}};

//overflow的滚动条一直处于最下方
var div=$(".entries");
div.scrollTop(div[0].scrollHeight);