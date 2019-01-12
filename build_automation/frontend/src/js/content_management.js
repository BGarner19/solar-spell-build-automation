import React from 'react';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import UploadContent from './upload_content';
import Snackbar from '@material-ui/core/Snackbar';
import BulkUploadContent from './bulk_upload_content';
import FileListComponent from './file_list_component';
import {buildMapFromArray} from './utils';
import {APP_URLS} from "./url";
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


class ContentManagement extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            description: "",
            fieldErrors: {},
            updatedTime: '',
            files: [],
            currentView: 'manage',
            content: null,
            tags: {},
            isLoaded: false,
        };
        this.setCurrentView = this.setCurrentView.bind(this);
        this.tagIdTagsMap = {};
        this.handleFileDelete = this.handleFileDelete.bind(this);
        this.saveContentCallback = this.saveContentCallback.bind(this);
        this.uploadNewFile = this.uploadNewFile.bind(this);
        this.handleContentEdit = this.handleContentEdit.bind(this);
        this.handleCloseSnackbar = this.handleCloseSnackbar.bind(this);
    }

    componentDidMount() {
        this.loadData()
    }
    buildTagIdTagsMap(tags) {
        // Builds a map of <Tag Id> - Tag
        const tagIdTagMap = {};
        Object.keys(tags).forEach(eachKey => {
            tagIdTagMap[eachKey] = buildMapFromArray(tags[eachKey], 'id');
        });
        return tagIdTagMap;
    }
    loadData() {
        const currInstance = this;
        const allRequests = [];
        allRequests.push(axios.get(APP_URLS.ALLTAGS_LIST, {responseType: 'json'}).then(function(response) {
            currInstance.tagIdTagsMap=currInstance.buildTagIdTagsMap(response.data);
            return response;
        }));
        allRequests.push(axios.get(APP_URLS.CONTENTS_LIST, {
            responseType: 'json'}));
        Promise.all(allRequests).then(function(values) {
            currInstance.setState({
                tags: values[0].data,
                files: values[1].data, isLoaded: true
            })
        }).catch(function(error) {
            console.error(error);
            console.error(error.response.data);
        });
    }
    handleTextFieldUpdate(stateProperty, evt) {
        const targetVal = evt.target.value;
        this.setState((prevState, props) => {
            const newState = {
                fieldErrors: prevState.fieldErrors,
                [stateProperty]: targetVal
            };
            newState.fieldErrors[stateProperty] = null;
            return newState;
        })
    }
    setCurrentView(viewName){
        this.setState({currentView: viewName})
    }
    handleFileDelete(file){
        this.setState((prevState, props)=>{
            const {files} = prevState;
            files.forEach(eachFile => {
                if (eachFile.id===file.id){
                    files.splice(files.indexOf(eachFile), 1)
                }
            });
            return {files, message: 'Delete Successful', messageType: 'info',};
        })
    }
    saveContentCallback(content, updated){
        const currInstance = this;
        axios.get(APP_URLS.ALLTAGS_LIST, {
            responseType: 'json'
        }).then(function (response) {
            currInstance.tagIdTagsMap=currInstance.buildTagIdTagsMap(response.data);
            currInstance.setState((prevState, props)=>{
                const {files} = prevState;
                if (updated){
                    files.forEach(eachFile => {
                        if (eachFile.id===content.id){
                            files.splice(files.indexOf(eachFile), 1, content);
                        }
                    });
                }
                else{
                    files.push(content);
                }
                return {
                    message: 'Save Successful',
                    messageType: 'info',
                    currentView: 'manage',
                    files,
                    tags: response.data
                }
            })
        }).catch(function (error) {
            console.error(error);
        });
    }
    uploadNewFile(){
        this.setState({
            currentView: 'upload',
            content: {
                id: -1,
                name: "",
                description: "",
                creators: [],
                coverages: [],
                subjects: [],
                keywords: [],
                workareas: [],
                languages: [],
                catalogers: [],
                updatedDate: new Date(),
                source: "",
                copyright: "",
                rightsStatement: "",
                originalFileName: ""
            }
        })
    }

    uploadBulkFiles() {
        this.setState({
            currentView: 'bulkUploadContent',
			contentArray: [],
			content: {
                id: -1,
                name: "",
                description: "",
                creators: [],
                coverages: [],
                subjects: [],
                keywords: [],
                workareas: [],
                languages: [],
                catalogers: [],
                updatedDate: new Date(),
                source: "",
                copyright: "",
                rightsStatement: "",
                originalFileName: ""
            }
        })
    }

    handleContentEdit(content){
        this.setState({
            currentView: 'upload',
            content: {
                id: content.id,
                name: content.name,
                description: content.description,
                creators: content.creators||[],
                coverages: content.coverage?[content.coverage]:[],
                subjects: content.subjects||[],
                keywords: content.keywords||[],
                workareas: content.workareas||[],
                languages: content.language?[content.language]:[],
                catalogers: content.cataloger?[content.cataloger]:[],
                updatedDate: this.parseDate(content.updated_time),
                source: content.source||'',
                copyright: content.copyright||'',
                rightsStatement: content.rights_statement||'',
                originalFileName: content.original_file_name,
            }
        })
    }
    parseDate(inputStr) {
        let splitval = inputStr.split("-");
        return new Date(splitval[0], splitval[1] - 1, splitval[2]);
    }

    render(){
        return (
            <div>
                <Grid container spacing={8} style={{paddingLeft: '20px'}}>
                    <Grid item xs={3} style={{paddingLeft: '20px'}}>
                        <h3>Content Management</h3>
                        <Button variant="contained" color="primary" onClick={e => {this.setCurrentView('manage')}}>
                            Manage Content
                        </Button>
                        <div style={{marginTop: '20px'}}> </div>
                        <Button variant="contained" color="primary" onClick={e => {this.uploadNewFile()}}>
                            Add Content
                        </Button>
                        <div style={{marginTop: '20px'}}> </div>
                        <Button variant="raised" color="primary" onClick={e => {this.uploadBulkFiles()}}>
                            Express Loading
                        </Button>
                    </Grid>

                    <Grid item xs={8}>
                        {this.state.isLoaded && this.state.currentView=='manage'&&<FileListComponent tags={this.state.tags} onEdit={this.handleContentEdit}
                                                                                                     onDelete={this.handleFileDelete} allFiles={this.state.files}
                                                                                                     tagIdsTagsMap={this.tagIdTagsMap} />}
                        {this.state.isLoaded && this.state.currentView=='upload'&&<UploadContent onSave={this.saveContentCallback}
                                                                                                 tagIdsTagsMap={this.tagIdTagsMap} allTags={this.state.tags}
                                                                                                 content={this.state.content}/>}

                        {this.state.isLoaded && this.state.currentView === 'bulkUploadContent' && <BulkUploadContent />}

                        {!this.state.isLoaded && 'loading'}
                    </Grid>
                </Grid>
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
            </div>
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
export default ContentManagement;
