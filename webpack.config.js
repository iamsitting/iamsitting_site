var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: {
    main: [
      './assets/js/index', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
    ]
  },

  output: {
    path: path.resolve('./iamsitting_site/static/bundles/'),
    filename: "[name].js",
    publicPath: 'http://localhost:3000/iamsitting_site/static/bundles/',
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment\/js$/), // to not to load all locales
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        }),
  ],

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: [/node_modules/],
        use: [{
          loader: 'babel-loader',
          query: { 'plugins': ['react-hot-loader/babel'], 'presets': ['react'] },
        }],
},
    ],
  },

  resolve: {
    modules: ['node_modules', 'bower_components'],
    extensions: ['.js', '.jsx']
  },
}