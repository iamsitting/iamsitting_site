var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: {
    main: [
      '../../iamsitting_site/templates/js/index', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
    ],
    blog_post: [
      '../../iamsitting_site/blog/static/blog/js/index'
    ]
  },

  output: {
    path: path.resolve(__dirname, '../../iamsitting_site/static/bundles/'),
    filename: "[name].js",
  },

  plugins: [
    new BundleTracker({path: __dirname, filename: './webpack-stats.json'}),
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment\/js$/), // to not to load all locales
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    }),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        use: [
          {
            loader: 'babel-loader',
          }
        ]
      }, //js, jsx
      {
        test: /\.woff2?$|\.ttf$|\.eot$|\.svg$|\.png$|\.jpg$|\.gif$/,
        loader: [
        {
          loader: 'file-loader',
          options: {
            name: '[name]-[hash].[ext]'
          }
        }
        ]
      }
    ],
  },

  resolve: {
    modules: [
      path.resolve(__dirname, '../node_modules'),
      path.resolve(__dirname, '../libraries'),
    ],
    alias: {
      jquery: "jquery/src/jquery"
    }
  }
}

