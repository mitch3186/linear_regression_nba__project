from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_trad_data (offset_vals):
    url = 'https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&player=&match=game&lg_id=NBA&year_min=2013&year_max=2020&team_id=MIN&opp_id=&is_range=N&is_playoffs=N&round_id=&best_of=&team_seed=&opp_seed=&team_seed_cmp=eq&opp_seed_cmp=eq&game_num_type=team&game_num_min=&game_num_max=&game_month=&game_location=&game_result=&is_overtime=&c1stat=ast_pct&c1comp=gt&c1val=0&c2stat=orb_pct&c2comp=gt&c2val=0&c3stat=tov_pct&c3comp=gt&c3val=0&c4stat=diff_pts&c4comp=lt&c4val=90&order_by=diff_pf&order_by_asc=&offset={}'
    bball_df = []
    
    for val in offset_vals:
        response = requests.get(url.format(val))
        page = response.text
        soup = BeautifulSoup(page,"lxml")
        table = soup.find_all('table')
        df = pd.read_html(str(table), header=1, index_col=0)
        df = pd.concat(df)
        df.drop_duplicates(subset='Date',keep=False,inplace=True)
        bball_df.append(df)
    return pd.concat(bball_df)


def get_non_score_data (offset_vals):
    url = 'https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&player=&match=game&lg_id=NBA&year_min=2013&year_max=2020&team_id=MIN&opp_id=&is_range=N&is_playoffs=N&round_id=&best_of=&team_seed=&opp_seed=&team_seed_cmp=eq&opp_seed_cmp=eq&game_num_type=team&game_num_min=&game_num_max=&game_month=&game_location=&game_result=&is_overtime=&c1stat=trb&c1comp=gt&c1val=0&c2stat=ast&c2comp=gt&c2val=0&c3stat=stl&c3comp=gt&c3val=0&c4stat=blk&c4comp=gt&c4val=0&order_by=tov&order_by_asc=&offset={}'
    bball_df = []
    
    for val in offset_vals:
        response = requests.get(url.format(val))
        page = response.text
        soup = BeautifulSoup(page,"lxml")
        table = soup.find_all('table')
        df = pd.read_html(str(table), header=1, index_col=0)
        df = pd.concat(df)
        df.drop_duplicates(subset='Date',keep=False,inplace=True)
        bball_df.append(df)
    return pd.concat(bball_df)


def drop_columns(names, dataframe):
    for name in names:
        dataframe.drop(name,axis=1,inplace=True)

def opp_col_rename(names, dataframe):
    for name in names:
        dataframe.rename(columns={name:'Opp '+name}, inplace = True)

def make_integers(names, dataframe):
    for name in names:
        dataframe[name] = dataframe[name].astype(int)

def rolling_avg_table(averages):
    avg_data_table = []

    for average in averages:
        df [average]= 