import React from 'react';

import DirectoryLayoutComponent from './directory_layout.js';
import ContentManagement from './content_management.js';
import DiskSpace from './diskspace.js';
import TagManagement from './tag_management.js';

import BuildProcessComponent from './build_process.js';
import Badge from '@material-ui/core/Badge';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import {APP_URLS} from "./url.js";
import axios from 'axios';

import solarSpellLogo from '../images/logo.png';
import '../css/style.css';

const styles = theme => ({
    padding: {
     padding: `0 ${theme.spacing.unit * 2}px`,
   },
});

class MainScreen extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentTab: 'dirlayout',
            showBadge: false
        };
        this.handleTabClick = this.handleTabClick.bind(this);
    }

    handleTabClick(event, selectedTab) {
        this.setState({ currentTab: selectedTab });
      };

    componentDidMount() {
        this.showBadge();
        this.timerID = setInterval(
            () => this.showBadge(),1000*60*60
        );
    }

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    showBadge() {
        axios
            .get(APP_URLS.DISKSPACE, {responseType: 'json'})
            .then((response) => {
                this.used = 100*(response.data.total_space-response.data.available_space)/response.data.total_space;
                const newState = ({completed: 100*(response.data.total_space-response.data.available_space)/response.data.total_space, showBadge: false});
                if(newState.completed > 80) {
                    newState.showBadge= true
                }
                this.setState(newState)
            })
            .catch((error) => {
                console.error(error);
                // TODO : Show the error message.
            });
    }

    render() {
        const currentTab = this.state.currentTab;
        const { classes } = this.props;

        return (
            <React.Fragment>
            <Grid container style={{backgroundColor: '#2196f3', height: '100px', flexGrow: 1, overflow: 'hidden'}} justify="center">
                <Grid item xs={12}>
                    <Grid container justify="center" alignItems="center" style={{height: '100%'}}>
                        <Grid item>
                            <img src={solarSpellLogo} className="spellLogo" />
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
            <Grid container style={{overflow: 'hidden', flexGrow: 1}}>
                <Grid item xs={12}>
                    <Paper>
                        <Tabs
                            value={currentTab}
                            indicatorColor="secondary"
                            onChange={this.handleTabClick}
                            textColor="secondary"
                            centered
                        >
                            <Tab value="tags" label="Metadata" />
                            <Tab value="contents" label="Contents" />
                            <Tab value="dirlayout" label="Library Versions" />
                            <Tab value="images" label="SolarSPELL Images" />
                            { this.state.showBadge ? (<Tab value="sysinfo" label= {
                                                    <Badge className= {classes.padding} color="secondary" badgeContent={'!'}>
                                                    System Info
                                                    </Badge>
                                                }/>) : (<Tab value="sysinfo" label="System Info" />)
                            }
                        </Tabs>
                    </Paper>
                </Grid>
            </Grid>
            <Grid container style={{marginTop: '20px'}}>
                <Grid item xs={12}>
                    {currentTab === 'dirlayout' && <DirectoryLayoutComponent />}
                    {currentTab === 'contents' && <ContentManagement />}
                    {currentTab === 'tags' && <TagManagement />}
                    {currentTab === 'images' && <BuildProcessComponent />}
                    {currentTab === 'sysinfo' && <DiskSpace />}
                </Grid>
            </Grid>
            </React.Fragment>
        );
    }
}

export default withStyles(styles)(MainScreen);
