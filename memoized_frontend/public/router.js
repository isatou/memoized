import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Posts from './Posts.jsx';
import AddPost from './AddPost.jsx';


export default function AppRoutes() {
  return (
    <Router>
      <Switch>
        <Route path="">
        </Route>
        <Route path="/posts">
        </Route>
        <Route path="/add-post">
        </Route>
      </Switch>
    </Router>
  )
}
