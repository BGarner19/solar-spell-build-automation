import React from 'react';
import Button from '@material-ui/Button';
import Grid from '@material-ui/Grid';
import AppBar from '@material-ui/AppBar';
import Typography from '@material-ui/Typography';
import TextField from '@material-ui/TextField';
import {APP_URLS, get_url} from "./url.js";
import Snackbar from '@material-ui/Snackbar';
import axios from 'axios';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        padding: theme.spacing.unit * 2,
        textAlign: 'center',
        color: theme.palette.text.secondary,
    },
    button: {
        margin: theme.spacing.unit,
    },
    input: {
        display: 'none',
    },
});


class BulkUploadMetadata extends React.Component{
    constructor(props) {
        super(props);
        this.state = {

            fieldErrors: {},

        };

        this.handleCloseSnackbar = this.handleCloseSnackbar.bind(this);

        this.handleFileSelection=this.handleFileSelection.bind(this);
        this.saveContent=this.saveContent.bind(this);
    }

    saveContent(evt) {

    }

    handleFileSelection(evt) {
        evt.persist();
        const file = evt.target.files;

        console.log(file);

        if (!Boolean(file)) { // If there is no file selected.
            return;
        }
        this.setState((prevState, props) => {
            const newState = {
                contentFile: file,
                contentFileName: file.name,
                fieldErrors: prevState.fieldErrors,
            };
            newState.fieldErrors['file'] = null;
            return newState;
        });

    }

    render(){
        return (
            <Grid item xs={8}>
                <AppBar position="static" style={{ height: '50px', margin: 'auto'}}>
                    <Typography gutterBottom variant="subtitle1" style={{color: '#ffffff', textAlign: 'center'}}>
                        Express Metadata Loading
                    </Typography>
                </AppBar>
                <div style={{marginTop: '20px'}}> </div>
                <TextField
                    id="contentFiles"
                    label="Content Files"
                    multiline
                    disabled
                    InputLabelProps={{
                        shrink: true,
                    }}
                    error={!!this.state.fieldErrors.file}
                    value={this.state.contentFileName}
                    margin="normal"
                />
                <input
                    accept="*"
                    className={'hidden'}
                    id="upload-file"
                    multiple
                    type="file"
                    ref={input => {this.fileInput = input;}}
                    onChange={this.handleFileSelection}
                />
                <label htmlFor="upload-file">
                    <Button variant="contained" component="span">
                        Browse
                    </Button>
                </label>

                <div style={{marginTop: '20px'}}> </div>
                <Button variant="contained" component="span" onClick={this.saveContent}>
                    Save
                </Button>

                <div style={{marginTop: '20px'}}> </div>
                <Snackbar
                    anchorOrigin={{
                        vertical: 'bottom',
                        horizontal: 'left',
                    }}
                    open={Boolean(this.state.message)}
                    onClose={this.handleCloseSnackbar}
                    message={<span>{this.state.message}</span>}
                    ContentProps={{
                        "style": this.getErrorClass()
                    }}
                />
            </Grid>
        )
    }
    getErrorClass() {
        return this.state.messageType === "error" ? {backgroundColor: '#B71C1C', fontWeight: 'normal'} : {};
    }

    handleCloseSnackbar() {
        this.setState({
            message: null,
            messageType: 'info'
        })
    }
}

export default BulkUploadMetadata;