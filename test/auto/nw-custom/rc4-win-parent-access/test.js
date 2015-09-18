  var win = window.open('about:blank');
  setTimeout(function() {
    console.log(win.parent);
    process.exit(0);
  }, 500); //maybe unstable
  win.close();



