/* jshint esversion: 6 */
/* eslint "require-jsdoc": ["error", {
    "require": {
        "FunctionDeclaration": false,
        "MethodDefinition": false,
        "ClassDeclaration": false,
        "ArrowFunctionExpression": false,
        "FunctionExpression": false
    }
}]*/
import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router} from 'react-router-dom';

import App from './App.jsx';

ReactDOM.render((
  <Router>
    <App />
  </Router>
), document.getElementById('root'))
