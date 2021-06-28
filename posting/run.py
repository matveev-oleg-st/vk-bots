#!/usr/bin/env python3

from datetime import datetime, timedelta, date
import pytz

if __name__ == "__main__":

    #dt_str   = 
    #print(dt_str)
    dt_base  = datetime.strptime(str(datetime.today()), "%Y-%m-%d  %H:%M:%S.%f")
    #pubdate  = dt_base.replace(tzinfo = pytz.UTC)
    #pubdate -= timedelta(hours=3)    
    #pubdate.strftime('%Y%m%d')
    pubdate  = format(dt_base, '%Y%m%d%H%M%S%f')
    print(pubdate)

#    print(type(format(pubdate, '%Y%m%d%H%M%S%f')))
    
#    #SELECT * FROM `main_news` WHERE `url` IN (SELECT `url` FROM `main_news` GROUP BY `url` HAVING COUNT(*) > 1) ORDER BY `url`
#    #DELETE FROM `main_news` as me, `main_news` as clone WHERE me.url = clone.url
#    DELETE FROM `main_news` USING `main_news`, `main_news` e1 where main_news.id > e1.id and main_news.url = e1.first_name
    
#    DELETE url FROM main_news t1 JOIN main_news t2 ON url.col = url.col AND t1.id < t2.id;
#    ALTER IGNORE TABLE main_news ADD UNIQUE (url)
#    SELECT `main_news`.* FROM `main_news` LEFT OUTER JOIN (SELECT MIN(`id`) AS `id`, `url` FROM `table` GROUP BY `url`) AS `tmp` ON `main_news`.`url` = `tmp`.`url` WHERE `tmp`.`url` IS NULL
#    DELETE FROM main_news WHERE SELECT main_news.* FROM main_news LEFT OUTER JOIN (SELECT MIN(id) AS id, url FROM main_news GROUP BY url) AS tmp ON main_news.url = tmp.url

#DELETE
#	`main_news`
#FROM  
#	`main_news`
#LEFT OUTER JOIN 
#	(SELECT MIN(`id`) AS `id`, `url` FROM `table` GROUP BY `url`) AS `tmp` 
#ON 
#	`table`.`id` = `tmp`.`id`  
#WHERE
#	`tmp`.`id` IS NULL    
