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
  int _selectedPage = 1;
  List _pageOptions = [
    Text('Forum', style: TextStyle(fontSize: 20)),
    HomePage(),
    Profile(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Talent Funding'),
      ),
      body: Center(
        child: _pageOptions[_selectedPage],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedPage,
        onTap: (int index) {
          setState(() {
            _selectedPage = index;
          });
        },
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.people),
            label: "Forum",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: "Home",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: "Profile",
          )
        ],
      ),
    );
  }
}

// This is the class that will define the HomePage
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Text('Homepage', style: TextStyle(fontSize: 20));
  }
}

class Profile extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(mainAxisAlignment: MainAxisAlignment.center, children: [
      Text('Profile ', style: TextStyle(fontSize: 20)),
      Text('', style: TextStyle(fontSize: 30)),
      Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Container(
            child: Text('Pic', style: TextStyle(fontSize: 20)),
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: Colors.white,
              border: Border.all(color: Colors.blue),
            ),
            height: 100,
            width: 100,
            alignment: Alignment.center,
          ),
          Container(
            child: Text('Skills', style: TextStyle(fontSize: 20)),
            decoration: BoxDecoration(
              color: Colors.white,
              border: Border.all(color: Colors.blue),
              borderRadius: BorderRadius.circular(10),
            ),
            height: 200,
            width: 150,
            alignment: Alignment.center,
          ),
        ],
      ),
      Container(
        child: Column(children: [
          Text('About me', style: TextStyle(fontSize: 20)),
          Text('', style: TextStyle(fontSize: 20)),
          Text('Any text describing the person will go here',
              style: TextStyle(fontSize: 10)),
        ]),
        decoration: BoxDecoration(
          color: Colors.white,
          border: Border.all(color: Colors.blue),
          borderRadius: BorderRadius.circular(10),
        ),
        padding: EdgeInsets.all(20),
        margin: EdgeInsets.all(20),
        width: 300,
        height: 400,
      ), //NEEDS TO IMPROVE
    ]);
  }
}

class Prototype extends StatefulWidget {
  @override
  PrototypeState createState() => PrototypeState();
}
