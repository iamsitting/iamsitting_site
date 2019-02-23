var webpack = require('webpack')
var WebpackDevServer = require('webpack-dev-server')
var devConfig = require('./webpack.development.config')

new WebpackDevServer(webpack(devConfig), {
  publicPath: devConfig.output.publicPath,
  hot: true,
  inline: true,
  historyApiFallback: true,
  headers: {
    'Access-Control-Allow-Origin': '*'
  }
}).listen(3000, '0.0.0.0', function (err, result){
  if (err) {
    console.log(err)
  }

  console.log('Listening at 0.0.0.0:3000')
})
