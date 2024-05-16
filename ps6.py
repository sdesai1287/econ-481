# %%
import sqlalchemy
from sqlalchemy import create_engine

# path = '/Users/sdesai/Desktop/econ-481/auctions.db'

import pandas as pd
from sqlalchemy.orm import Session

# class DataBase:
#     def __init__(self, loc: str, db_type: str = "sqlite") -> None:
#         """Initialize the class and connect to the database"""
#         self.loc = loc
#         self.db_type = db_type
#         self.engine = create_engine(f'{self.db_type}:///{self.loc}')
#     def query(self, q: str) -> pd.DataFrame:
#         """Run a query against the database and return a DataFrame"""
#         with Session(self.engine) as session:
#             df = pd.read_sql(q, session.bind)
#         return(df)

# auctions = DataBase(path)


# %%
def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/sdesai1287/econ-481/blob/main/ps6.py"
github()

# %%
def std() -> str:
    """
    Some docstrings.
    """
    query = """
        SELECT itemId, 
            SQRT(SUM(POWER((bidAmount - avgb), 2)) / (COUNT(bidAmount) - 1)) AS std
        FROM (
            SELECT itemId,
                bidAmount,
                AVG(bidAmount) OVER(PARTITION BY itemId) as avgb
            FROM bids
        )
        GROUP BY itemId
        HAVING (std is not null)
        """
    return query
# auctions.query(std())

# %%
def bidder_spend_frac() -> str:
    """
    Some docstrings.
    """
    

    query = """
    SELECT 
        rb.bidderName,
        SUM(CASE WHEN rb.highBidderName = rb.bidderName THEN rb.bidamount ELSE 0 END) AS total_spend,
        SUM(rb.bidamount) AS total_bids,
        CAST(SUM(CASE WHEN rb.highBidderName = rb.bidderName THEN rb.bidamount ELSE 0 END) AS REAL) / CAST(SUM(rb.bidamount) AS REAL) AS spend_frac
    FROM (
        SELECT 
            bidderName, 
            bidamount, 
            highBidderName,
            ROW_NUMBER() OVER (PARTITION BY itemId, bidderName ORDER BY bidamount DESC) AS row_num
        FROM bids
    ) AS rb
    WHERE rb.row_num = 1
    GROUP BY rb.bidderName;
   """
    return query
# auctions.query(bidder_spend_frac())


# %%
def min_increment_freq() -> str:
    """
    Generates a SQL query to calculate the frequency of bids that are exactly
    the minimum bid increment above the previous high bid.
    """

    sql_query = """
    SELECT 
        SUM(CASE 
                WHEN b2.bidAmount = b1.bidAmount + i.bidIncrement THEN 1
                ELSE 0
            END) * 1.0 / COUNT(b2.bidAmount) AS freq
    FROM bids b1
    JOIN items i ON i.itemId = b1.itemId
    JOIN bids b2 ON b1.bidAmount < b2.bidAmount AND b1.itemId = b2.itemId;
        """

    return sql_query
# auctions.query(min_increment_freq())

# %%
def win_perc_by_timestamp() -> str:
    query = """
    WITH BidStats AS (
    SELECT
        b.itemId,
        b.bidAmount,
        b.bidTime,
        t.startTime,
        t.endTime,
        CASE
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.1 THEN 1
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.2 THEN 2
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.3 THEN 3
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.4 THEN 4
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.5 THEN 5
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.6 THEN 6
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.7 THEN 7
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.8 THEN 8
            WHEN (julianday(t.endTime) - julianday(b.bidTime)) / (julianday(t.endTime) - julianday(t.startTime)) < 0.9 THEN 9
            ELSE 10
        END AS timestamp_bin
    FROM bids b
    JOIN (
        SELECT itemId, MIN(bidTime) AS startTime, MAX(bidTime) AS endTime
        FROM bids
        GROUP BY itemId
    ) AS t ON b.itemId = t.itemId
),
WinningBids AS (
    SELECT itemId, MAX(bidAmount) AS highestBidAmount
    FROM bids
    GROUP BY itemId
)
SELECT
    bs.timestamp_bin,
    100.0 * SUM(CASE WHEN bs.bidAmount = wb.highestBidAmount THEN 1 ELSE 0 END) / COUNT(*) AS win_perc
FROM BidStats bs
JOIN WinningBids wb ON bs.itemId = wb.itemId
GROUP BY bs.timestamp_bin;
"""
    return query
    
# auctions.query(win_perc_by_timestamp())


