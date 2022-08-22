select * from players_player where full_name like '%McKissic%' 
select * from ranks where player_id is null

UPDATE ranks
set name = REPLACE([name], '.', '')

UPDATE ranks
set name = REPLACE([name], 'Jr', '')

UPDATE ranks
set name = 'A.J. Brown'
where name = 'AJ Brown'

UPDATE ranks
set name = 'J.K. Dobbins'
where name = 'JK Dobbins'

UPDATE ranks
set name = 'Allen Robinson'
where name = 'Allen Robinson II'

UPDATE ranks set name = 'Amon-Ra St. Brown'
where name = 'Amon-Ra St Brown'

UPDATE ranks set name = 'Gabe Davis'
where name = 'Gabriel Davis'

UPDATE ranks set name = 'T.J. Hockenson'
where name = 'TJ Hockenson'

UPDATE ranks set name = 'Melvin Gordon'
where name = 'Melvin Gordon III'

UPDATE ranks set name = 'Mitch Trubisky'
where name = 'Mitchell Trubisky'

UPDATE ranks set name = 'K.J. Osborn'
where name = 'KJ Osborn'

UPDATE ranks set name = 'C.J. Uzomah'
where name = 'CJ Uzomah'

UPDATE ranks set name = 'J.D. McKissic'
where name = 'JD McKissic'

UPDATE ranks 
SET player_id = (SELECT top 1 player_id 
FROM players_player 
WHERE [ranks].[Name] = players_player.full_name)



INSERT INTO ranks_playerrank(rank, player_id, full_name, team, position, adp, adpDelta, positionalRank) 
SELECT Overall_Rank, player_id, Name, Team, position, ADP, ADP_Delta, Positional_Rank
from ranks