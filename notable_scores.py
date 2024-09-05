import pandas as pd
from pandasql import sqldf

ms_df = pd.read_csv('stats_csv.csv')

query = """
        WITH STNB_ALL AS
            (
                SELECT  mode AS Mode, 
                        style AS Style,
                        MAX(47.299/(POWER(Time, 1.7)/BBBV)) AS STNB
                FROM ms_df
                WHERE Mode = 'BEG'
                GROUP BY Style
                UNION ALL
                SELECT  mode AS Mode, 
                        style AS Style,
                        MAX(153.73/(POWER(Time, 1.7)/BBBV)) AS STNB
                FROM ms_df
                WHERE Mode = 'INT'
                GROUP BY Style
                UNION ALL
                SELECT  mode AS Mode, 
                        style AS Style,
                        MAX(435.001/(POWER(Time, 1.7)/BBBV)) AS STNB
                FROM `ms_df`
                WHERE Mode = 'EXP'
                GROUP BY Style
            )
        
        SELECT  m.mode AS Mode, 
                m.style AS Style, 
                COUNT(*) AS Games,
                MIN(Time) AS Time,
                MAX(BBBV/Time) AS '3bv/s',
                MAX(BBBV*1.0/(Lcl+Rcl+Dcl)) AS IOE,
                MIN((Time+1)/BBBVs) AS RQP,
                STNB,
                MIN(Openings) AS MinOps,
                MAX(Openings) AS MaxOps
        FROM ms_df as m
        INNER JOIN `STNB_ALL` AS b
            ON  m.mode = b.Mode AND
                m.style = b.Style
        GROUP BY m.Mode, m.Style
        ORDER BY IOE DESC;
        """
    
print("Notable Scores")
results = sqldf(query, locals())
print(results.to_markdown(index=False, tablefmt="github", floatfmt=("", "", "", ".2f", ".3f", ".4f", ".3f", ".2f")))

