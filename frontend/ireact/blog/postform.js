import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from "react-redux"
import { applyMiddleware, createStore, compose } from "redux"
import thunkMiddleware from 'redux-thunk'
import initialState from "ireact/blog/utils/initialState"
import reducer from "ireact/blog/utils/reducer"
import { AppContainer } from "react-hot-loader"
import { BlogCMS } from "ireact/blog/components/BlogCMS"


const postformRoot = document.getElementById('root');
const store = createStore(reducer, initialState, compose(
  applyMiddleware(thunkMiddleware),
  window.devToolsExtension ? window.devToolsExtension() : f => f
));
window.store = store;

let render = (Component, reactRoot) => {
  if (!reactRoot) {
    return;
  }
  ReactDOM.render(
    <Provider store={store}>
      <Component />
    </Provider>,
    reactRoot
  )
}


if(module.hot) {
  // Support hot reloading of components
  // and display an overlay for runtime errors
  const renderApp = render;
  const renderError = (error) => {
    const RedBox = require("redbox-react");
      ReactDOM.render(
        <RedBox error={error} />,
        rootEl,
      );
  };

  render = () => {
    try {
      renderApp(BlogCMS, postformRoot);
    }
    catch(error) {
      renderError(error);
    }
  };

  module.hot.accept("ireact/blog/components/BlogCMS", () => {
    setTimeout(render, BlogCMS, postformRoot);
  });
}

render(BlogCMS, postformRoot);
