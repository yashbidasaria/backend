# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class dataset_meta(models.Model):
    name = models.CharField(primary_key=True)
    info = models.CharField()
    schema = models.CharField()
    price = models.CharField()
    seller = models.CharField()
    tags = models.CharField()

    class Meta:
        db_table = 'data_with_tags'

class crash_meta(models.Model):
    Age = models.IntegerField()
    Alcohol_Results = models.FloatField()
    Atmospheric_Condition = models.CharField()
    Crash_Date = models.DateTimeField()
    Drug_Involvement = models.CharField()
    Fatalities_in_Crash = models.IntegerField()
    First_Harmful_Event = models.CharField()
    Gender = models.CharField()
    ID = models.IntegerField()
    Injury_Severity = models.CharField()
    Person_Type = models.CharField()
    Race = models.CharField()
    Roadway = models.CharField()
    State = models.CharField()
    PK = models.CharField()

    class Meta:
        db_table = 'crash'
        app_label = '1'

class dblp_meta(models.Model):
    FromNodeId = models.IntegerField()
    ToNodeId = models.IntegerField()
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'dblp'
        app_label = '2'


class world_city_meta(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField()
    CountryCode = models.CharField()
    District = models.CharField()
    Population = models.BigIntegerField()

    class Meta:
        db_table = 'city'
        app_label = '3'


class world_country_meta(models.Model):
    Code = models.CharField(primary_key=True)
    Name = models.CharField()
    Continent = models.CharField()
    Region = models.CharField()
    SurfaceArea = models.FloatField()
    IndepYear = models.SmallIntegerField()
    Population = models.IntegerField()
    LifeExpectancy = models.FloatField()
    GNP = models.FloatField()
    GNPOld = models.FloatField()
    LocalName = models.CharField()
    GovernmentForm = models.CharField()
    HeadOfState = models.CharField()
    Capital = models.IntegerField()
    Code2 = models.CharField()

    class Meta:
        db_table = 'country'
        app_label = '3'


class world_countryLang_meta(models.Model):
    CountryCode = models.CharField(primary_key=True)
    Language = models.CharField()
    IsOfficial = models.BooleanField()
    Percentage = models.FloatField()

    class Meta:
        db_table = 'countrylanguage'
        app_label = '3'


class ssb_customer(models.Model):
    c_custkey = models.IntegerField(primary_key=True)
    c_name = models.CharField()
    c_address = models.CharField()
    c_city = models.CharField()
    c_nation = models.CharField()
    c_region = models.CharField()
    c_phone = models.CharField()
    c_mktsegment = models.CharField()

    class Meta:
        db_table = 'customer_ssb'
        app_label = '4'


class ssb_dwdate(models.Model):
    d_datekey = models.IntegerField(primary_key=True)
    d_date = models.CharField()
    d_dayofweek = models.CharField()
    d_month = models.CharField()
    d_year = models.IntegerField()
    d_yearmonthnum = models.IntegerField()
    d_yearmonth= models.CharField()
    d_daynuminweek = models.IntegerField()
    d_daynuminmonth  = models.IntegerField()
    d_daynuminyear = models.IntegerField()
    d_monthnuminyear = models.IntegerField()
    d_weeknuminyear = models.IntegerField()
    d_sellingseason  = models.CharField()
    d_lastdayinweekfl = models.CharField()
    d_lastdayinmonthfl = models.CharField()
    d_holidayfl  = models.CharField()
    d_weekdayfl  = models.CharField()

    class Meta:
        db_table = 'dwdate'
        app_label = '4'

class ssb_lineorder(models.Model):
    lo_orderkey = models.IntegerField()
    lo_linenumber = models.IntegerField()
    lo_custkey = models.IntegerField()
    lo_partkey = models.IntegerField()
    lo_suppkey = models.IntegerField()
    lo_orderdate = models.IntegerField()
    lo_orderpriority = models.CharField()
    lo_shippriority = models.CharField()
    lo_quantity = models.IntegerField()
    lo_extendedprice = models.IntegerField()
    lo_ordertotalprice = models.IntegerField()
    lo_discount = models.IntegerField()
    lo_revenue = models.IntegerField()
    lo_supplycost = models.IntegerField()
    lo_tax = models.IntegerField()
    lo_commitdate = models.IntegerField()
    lo_shipmode = models.CharField()
    lo_pk = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'lineorder'
        app_label = '4'


class ssb_part(models.Model):
    p_partkey = models.IntegerField(primary_key=True)
    p_name = models.CharField()
    p_mfgr = models.CharField()
    p_category = models.CharField()
    p_brand1 = models.CharField()
    p_color = models.CharField()
    p_type = models.CharField()
    p_size = models.IntegerField()
    p_container = models.CharField()

    class Meta:
        db_table = 'part'
        app_label = '4'

class ssb_supplier(models.Model):
    s_suppkey = models.IntegerField(primary_key=True)
    s_name = models.CharField()
    s_address = models.CharField()
    s_city = models.CharField()
    s_nation = models.CharField()
    s_region = models.CharField()
    s_phone = models.CharField()

    class Meta:
        db_table = 'supplier'
        app_label = '4'

class tpch_customer(models.Model):
    c_custkey = models.IntegerField(primary_key=True)
    c_name = models.CharField()
    c_address = models.CharField()
    c_nationkey = models.IntegerField()
    c_phone = models.CharField()
    c_acctbal = models.IntegerField()
    c_mktsegment = models.CharField()
    c_comment = models.CharField()

    class Meta:
        db_table = 'customer'
        app_label = '5'


class tpch_lineitem(models.Model):
    l_orderkey = models.IntegerField()
    l_partkey = models.IntegerField()
    l_suppkey = models.IntegerField()
    l_linenumber = models.IntegerField()
    l_quantity = models.DecimalField()
    l_extendedprice = models.DecimalField()
    l_discount = models.DecimalField()
    l_tax = models.DecimalField()
    l_returnflag = models.CharField()
    l_linestatus = models.CharField()
    l_shipdate = models.DateField()
    l_commitdate = models.DateField()
    l_receiptdate = models.DateField()
    l_shipinstruct = models.CharField()
    l_shipmode = models.CharField()
    l_comment = models.CharField()
    l_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'lineitem'
        app_label = '5'


class tpch_nation(models.Model):
    n_nationkey = models.IntegerField(primary_key=True)
    n_name = models.CharField()
    n_regionkey = models.IntegerField()
    n_comment = models.CharField()

    class Meta:
        db_table = 'nation'
        app_label = '5'

class tpch_orders(models.Model):
    o_orderkey = models.IntegerField(primary_key=True)
    o_custkey = models.IntegerField()
    o_orderstatus = models.CharField()
    o_totalprice = models.DecimalField()
    o_orderdate = models.DateField()
    o_orderpriority = models.CharField()
    o_clerk = models.CharField()
    o_shippriority = models.IntegerField()
    o_comment  = models.CharField()

    class Meta:
        db_table = 'orders'
        app_label = '5'

class tpch_part(models.Model):
    p_partkey = models.IntegerField(primary_key=True)
    p_name = models.CharField()
    p_mfgr = models.CharField()
    p_brand = models.CharField()
    p_type = models.CharField()
    p_size = models.IntegerField()
    p_container = models.CharField()
    p_retailprice = models.IntegerField()
    p_comment = models.CharField()

    class Meta:
        db_table = 'part'
        app_label = '5'

class tpch_partsupp(models.Model):
    ps_partkey = models.IntegerField(primary_key=True)
    ps_suppkey = models.IntegerField()
    ps_availqty = models.IntegerField()
    ps_supplycost = models.IntegerField()
    ps_comment = models.CharField()
    ps_id = models.IntegerField()

    class Meta:
        db_table = 'partsupp'
        app_label = '5'

class tpch_region(models.Model):
    r_regionkey = models.IntegerField(primary_key=True)
    r_name = models.CharField()
    r_comment = models.CharField()

    class Meta:
        db_table = 'region'
        app_label = '5'

class tpch_supplier(models.Model):
    s_suppkey = models.IntegerField(primary_key=True)
    s_name = models.CharField()
    s_address = models.CharField()
    s_nationkey = models.IntegerField()
    s_phone = models.CharField()
    s_acctbal = models.IntegerField()
    s_comment = models.CharField()

    class Meta:
        db_table = 'supplier'
        app_label = '5'