import React from "react";
import ReactDOM from "react-dom";
import {Provider} from "react-redux";
import {createStore, compose} from 'redux';
import initialState from 'ireact/blog/utils/initialState';
import reducer from 'ireact/blog/utils/reducer';
import {AppContainer} from 'react-hot-loader';

const store = createStore(reducer, initialState, compose(
  window.devToolsExtension ? window.devToolsExtension() : f => f
));
window.store = store;

function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="world" />;

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
  element, postformRoot
);

