// Code that serves as base for Talent Funding prototype

import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Prototype',
      home: Prototype(),
    );
  }
}

class PrototypeState extends State<Prototype> {
  final List<String> headers = ["Home", "Forum", "Profile", "Exit"]; // Elements
  final TextStyle _biggerFont = const TextStyle(fontSize: 18);
  @override
  Widget build(BuildContext context) {
    return Scaffold (
      appBar: AppBar(
        title: Text('Prototype'),
      ),
      body: buildHeaders(),
    );
  }

  Widget buildHeaders() {
    // iterates over all list items
    return ListView.builder(
        itemCount: 2 * headers.length, // Specify the length of the list
        padding: const EdgeInsets.all(16),
        itemBuilder: (BuildContext _context, int i) {
          if (i.isOdd) {
            return Divider();
          }
          final int index = i ~/ 2;
          return buildRow(headers[index]);
        });
  }

  Widget buildRow(String element) {
    return ListTile(
      title: Text(
        element,
        style: _biggerFont,
      ),
    );
  }
}

class Prototype extends StatefulWidget {
  @override
  PrototypeState createState() => PrototypeState();
}
