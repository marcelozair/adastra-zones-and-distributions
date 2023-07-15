const webpack = require('webpack');

const path = require('path');

const { WebpackManifestPlugin } = require('webpack-manifest-plugin');

const { VueLoaderPlugin } = require('vue-loader');

const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {

  cache: false,

  entry: {
    'app': './resources/js/app.js',
    'layout/app': './resources/js/layout/app/index.js',
    'pages/test/home': './resources/js/pages/test/home/index.js',
  },

  output: {
    path: path.resolve('./static/build'),
    filename: '[name].[chunkhash].js',
    clean: true
  },

  resolve: {
    alias: {
	    'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' para webpack 1
  	}
  },

  module:{
    rules: [
      {
        test: /\.vue$/,
          loader: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader'
        ]
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          {
            loader: 'sass-loader',
            options: {
              // Prefer `dart-sass`
              implementation: require('sass'),
            },
          },
        ]
      }
    ]
  },

  plugins: [
    new VueLoaderPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name].[chunkhash].css',
      chunkFilename: '[id].css'
    }),
    new WebpackManifestPlugin({
      publicPath : 'build/'
    })
  ],

  optimization: {

  },
};
