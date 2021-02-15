import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Prototype',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Prototype 1'),
        ),
        body: Center(
          child: Prototype(),
        ),
      ),
    );
  }
}

class PrototypeState extends State<Prototype> {
  @override
  Widget build(BuildContext context) {
    final Text content = Text('It is working...');
    return content;
  }
}

class Prototype extends StatefulWidget {
  @override
  PrototypeState createState() => PrototypeState();
}
