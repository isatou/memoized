/*import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;*/

/*
 import React from 'react';
 import { Editor } from '@tinymce/tinymce-react';

 class App extends React.Component {
   handleEditorChange = (content, editor) => {
     console.log('Content was updated:', content);
   }

   render() {
     return (
       <Editor
         initialValue="<p>This is the initial content of the editor</p>"
         init={{
           height: 500,
           menubar: false,
           plugins: [
             'advlist autolink lists link image charmap print preview anchor',
             'searchreplace visualblocks code fullscreen',
             'insertdatetime media table paste code help wordcount'
           ],
           toolbar:
             'undo redo | formatselect | bold italic backcolor | \
             alignleft aligncenter alignright alignjustify | \
             bullist numlist outdent indent | removeformat | help'
         }}
         onEditorChange={this.handleEditorChange}
       />
     );
   }
 }

 export default App;
 */

 import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Posts from './components/Posts.jsx';
import AddHowTo from './components/AddHowTo.jsx';
import AddLessonLearnt from './components/AddLessonLearnt.jsx';
import AddResource from './components/AddResource.jsx';
import Container from './components/Container.jsx';
import MenuBar from './components/MenuBar.jsx';


export default function AppRoutes() {
  return (
    <Router>
      <MenuBar />
      <Switch>
        <Route exact path="/">
          <Posts />
        </Route>
        <Route path="/posts">
          <Posts />
        </Route>
        <Route path="/add-how-to">
          <AddHowTo />
        </Route>
        <Route path="/add-lesson-learnt">
          <AddLessonLearnt />
        </Route>
        <Route path="/add-resource">
          <AddResource />
        </Route>
      </Switch>
    </Router>
  )
}

