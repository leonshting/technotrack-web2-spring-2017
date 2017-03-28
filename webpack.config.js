/**
 * Created by leonshting on 23.03.17.
 */

const webpack = require('webpack');
const path = require('path');


const NODE_ENV = process.env.NODE_ENV || 'development';
module.exports = {
    entry: {
        app: './index.jsx'
    },
    context: path.join(__dirname, 'static_src'),
    output: {
        filename: '[name].js',
        path: path.join(__dirname, 'static/build')
    },
    module: {
        loaders: [
            {
                test: /\.(js|jsx)$/,
                include: /static_src/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['react', 'es2015', 'stage-0']
                }
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },
        ]
    },

    plugins: (NODE_ENV !== 'development') ? [
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false,
                drop_console: false,
                unsafe: true,
            },
        })
    ] : [
        new webpack.NoEmitOnErrorsPlugin(),
    ],
    //TODO: bundletracker for getting different verions of app

    watch: NODE_ENV === 'development',
    devtool: NODE_ENV === 'development' ? 'cheap-module-inline-source-map' : false,
};

