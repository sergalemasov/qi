# -*- coding: utf-8 -*-

prom = u'''
    inner join
            (
            select
                dp.parent_id
            from
                i_collect.dbo.debt_promise as dp
                left join
                        (
                            select
                                dp2.id as id
                                ,(case
                                    when (dp2.prom_sum is not null)
                                    then 1
                                    else 0
                                end) as kol_ob
                            from
                                i_collect.dbo.debt_promise as dp2
                            group by
                                dp2.id,
                                dp2.prom_sum
                        )dp2    on dp2.id=dp.id
            where
                dp.dt %s
            group by
                dp.parent_id
            having
                sum(dp2.kol_ob) %s
            )dp
                on d.id = dp.parent_id\n'''

mprom = u'''
    inner join
            (
            select
                dp.parent_id
            from
                i_collect.dbo.debt_promise as dp
            where
                (dp.cover_sum = 0 or dp.cover_sum is null)
                and dp.dt %s
            group by
                dp.parent_id
            having count(dp.id) %s
            )dp_miss
                on dp_miss.parent_id = d.id\n'''

calc = u'''
    inner join
            (
            select
                dc.parent_id
            from
                [i_collect].[dbo].[debt_calc] as dc
                left join(
                    select
                        dc2.id as id
                        ,(case
                            when(
                                dc2.int_sum is not null
                                and dc2.is_confirmed = 1
                                and dc2.is_cancel = 0
                            )
                            then dc2.int_sum
                            else 0
                            end
                        ) as PP_sum
                        ,(case
                            when(
                                dc2.int_sum is not null
                                and dc2.is_confirmed = 1
                                and dc2.is_cancel = 0
                            )
                            then 1
                            else 0
                            end
                        ) as PP_kolvo
                    from
                        [i_collect].[dbo].[debt_calc] as dc2
                    group by
                        dc2.is_confirmed,
                        dc2.int_sum,
                        dc2.id,
                        dc2.is_cancel
                ) dc2
                    on dc2.id=dc.id
                where
                    dc.calc_date %s
                group by
                    dc.parent_id
                having
                    sum(dc2.PP_kolvo) %s
                    and sum(dc2.PP_sum) %s
            )dc
                on dc.parent_id = d.id'''

phone = u'''
    inner join
            (
            /*return parametres phone numbers*/
            select
                ph.parent_id
                ,ph.number
            from
                i_collect.dbo.phone ph
            where
                ph.typ %s
                and ph.status %s
            )ph
                on ph.parent_id = per.id'''


perspect = u'''
    inner join
            (
            select
                c.r_debt_id
            from
                contact_log c
            where
                c.typ in (1,3)
                and c.dt %s
                and cl.result in(
                1,2,4,5,11,12,14,15,16,201,202,204,207,208,210,212,213,706,
                707,712,714,715,717,718,719,720,721,723,726,729,737,738,739,
                740,816,817,818,819,820,821,824,825,826,838,839,840,842,861,
                862,863,865,866,867,868,870,874,875,877,880,120154,120155,
                120156,120183,120186,120187,120188,120189,120190,120191,120193,
                120194,120197,120198,120199,120200,120201,120202,120205,120206,
                120207,120214,120215,120216,120217,120218,120221,120222,120223,
                120224,120225,120226,120227,120228,120231,120233,120234,120235,
                120237,120239,120240,120241,320157,320161,320272,320273,320274,
                320280,320283,320284,320287,320297,320300,320301,320304,320310,
                320311,320313,320316,320317,320318,320319,320320,320322,320712,
                320607,320616,320609,320713,320614,320617,320610,320714,320635,
                320704,320637,320715,320640,320705,320710,321084,321023,321024,
                21025,321137,321138,321139,321140,321057,321034,321032,321028,
                321035,321033,321031,321027,321142,321143,321144,321145,321083,
                321078,321073,321085,321082,321077,321072,321062,321081,321076,
                321071,321061,321147,321148,321149,321150,321080,321075,321070,
                321086,321079,321074,321069,321060,321022,321021,321020,321017,
                321152,321153,321154,321155,320879,320880,320881,320882,320929,
                320927,320925,320930,320928,320926,320924,320921,321158,321159,
                321160,321161,320920,320919,320918,321157,320917,320916,320915,
                320912,320910,320909,320908,320905,321164,321165,321166,321167,
                320903,320902,320901,321163,320900,320899,320898,320895,320893,
                320892,320891,320888,321226,321225,321223,321224,321221,321220,
                321219,321218,321215,320936,320938,320932,321213,321212,321211,
                321210,321209,321208,321207,321206,321205,321202,321200,321199,
                321198,321195,321183,321181,321179,321178,321177,321176,321175,
                321174,321173,320935,320937,320931
                --феникс
                ,321513,321457,321458,321459,321486,321484,321482,321462,321485,
                321483,321465,321461,321512,321507,321502,321514,321511,321506,
                321501,321491,321510,321505,321500,321490,321509,321504,321499,
                321515,321508,321503,321498,321489,321456,321455,321454,321451
                --МТС
                ,320712,320607,320616,320609,320713,320614,320617,320610,320714,
                320635,320704,320637,320715,320640,320705,320710)
                )
            group by
                c.r_debt_id
            having count(c.id) %s
            )persp
                on persp.r_debt_id = d.id\n'''