import 'dart:io';
import 'dart:convert';

void main() {
  Socket.connect("127.0.0.1", 8080).then((socket) {
    print('Connected to: '
      '${socket.remoteAddress.address}:${socket.remotePort}');
    socket.add(utf8.encode('hello'));
    socket.destroy();
  });
}