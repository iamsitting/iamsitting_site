import React from "react";
import ReactDOM from "react-dom";
import {Provider} from "react-redux";
import {createStore, compose} from "redux";
import initialState from "ireact/blog/utils/initialState";
import reducer from "ireact/blog/utils/reducer";
import {AppContainer} from "react-hot-loader";
import BlogCMS from "ireact/blog/components/BlogCMS";

const store = createStore(reducer, initialState, compose(
  window.devToolsExtension ? window.devToolsExtension() : f => f
));
window.store = store;

const render = (Component, reactRoot) => {
  if (!reactRoot) {
    return;
  }
  ReactDOM.render(
    <AppContainer>
      <Provider store={store}>
        <Component />
      </Provider>,
    </AppContainer>,
    reactRoot
  )
}

let postformRoot = document.getElementById('react-root');

render(
  BlogCMS, postformRoot
);

if (module.hot) {
  module.hot.accept("ireact/blog/components/BlogCMS"), () => {
    render(BlogCMS, postformRoot);
  }
}