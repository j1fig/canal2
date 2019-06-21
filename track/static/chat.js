let conn = null;
let name = "UNKNOWN";

let log = (msg) => {
  let control = $('#log');
  let date = new Date();
  let date_prompt = '(' + date.toISOString().split('T')[1].slice(0,8) + ') ';
  control.html(control.html() + date_prompt + msg + '<br/>');
  control.scrollTop(control.scrollTop() + 1000);
}

let connect = () => {
  disconnect();
  let wsUri = (window.location.protocol=='https:'&&'wss://'||'ws://')+window.location.host+'/ws';
  conn = new WebSocket(wsUri);
  //log('Connecting...');
  conn.onopen = function() {
    //log('Connected.');
    update_ui();
  };
  conn.onmessage = function(e) {
    let data = JSON.parse(e.data);
    switch (data.action) {
      case  'connect':
        name = data.name;
        log('Connected as ' + name);
        update_ui();
        break;
      case  'disconnect':
        name = data.name;
        log('Disconnected ' + name);
        update_ui();
        break;
      case 'join':
        log('Joined ' + data.name);
        break;
      case 'sent':
        log(data.name + ': ' + data.text);
        break;
    }
  };
  conn.onclose = function() {
    log('Disconnected.');
    conn = null;
    update_ui();
  };
}

let disconnect = () => {
  if (conn != null) {
    //log('Disconnecting...');
    conn.close();
    conn = null;
    name = 'UNKNOWN';
    update_ui();
  }
}

let update_ui = () => {
  if (conn == null) {
    $('#status').text('disconnected');
    $('#connect').html('Connect');
    $('#send').prop("disabled", true);
  } else {
    $('#status').text('connected (' + conn.protocol + ')');
    $('#connect').html('Disconnect');
    $('#send').prop("disabled", false);
  }
  $('#name').text(name);
}

let init = () => {
  $('#connect').on('click', function() {
    if (conn == null) {
      connect();
    } else {
      disconnect();
    }
    update_ui();
    return false;
  });
  $('#send').on('click', function() {
    let text = $('#text').val();
    // log('Sending: ' + text);
    log(text);
    conn.send(text);
    $('#text').val('').focus();
    return false;
  });
  $('#text').on('keyup', function(e) {
    if (e.keyCode === 13) {
      $('#send').click();
      return false;
    }
  });
}

export {init};
