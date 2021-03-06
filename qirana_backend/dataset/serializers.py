from rest_framework import serializers
from qirana_backend.dataset.models import dataset_meta, crash_meta, dblp_meta, world_city_meta, world_country_meta, \
    world_countryLang_meta, ssb_customer, ssb_dwdate, ssb_lineorder, ssb_part, ssb_supplier, tpch_customer, tpch_lineitem, tpch_nation, tpch_part, tpch_orders, tpch_partsupp, tpch_region, tpch_supplier
#from django.db import models


class nameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = dataset_meta
        fields = ('name', 'schema', 'price', 'seller', 'info', 'tags')

class dblpSerializer(serializers.ModelSerializer):

    class Meta:
        model = dblp_meta
        fields = ('FromNodeId', 'ToNodeId', 'id')

class crashSerializer(serializers.ModelSerializer):

    class Meta:
        model = crash_meta
        fields = ('Age', 'Alcohol_Results', 'Atmospheric_Condition', 'Crash_Date', 'Drug_Involvement', 'Fatalities_in_Crash', 'First_Harmful_Event', 'Gender', 'ID', 'Injury_Severity', 'Person_Type', 'Race', 'Roadway', 'State', 'PK')

class worldCitySerializer(serializers.ModelSerializer):

    class Meta:
        model = world_city_meta
        fields = ('ID', 'Name', 'CountryCode', 'District', 'Population')

class worldCountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = world_country_meta
        fields = ('Code', 'Name', 'Continent', 'Region', 'SurfaceArea', 'IndepYear', 'Population', 'LifeExpectancy', 'GNP', 'GNPOld', 'LocalName', 'GovernmentForm', 'HeadOfState', 'Capital', 'Code2')

class worldLangSerializer(serializers.ModelSerializer):

    class Meta:
        model = world_countryLang_meta
        fields = ('CountryCode', 'Language', 'IsOfficial', 'Percentage')

class ssb_customerSer(serializers.ModelSerializer):

    class Meta:
        model = ssb_customer
        fields = ('c_custkey', 'c_name', 'c_address', 'c_city', 'c_nation', 'c_region', 'c_phone', 'c_mktsegment')

class ssb_dwdateSer(serializers.ModelSerializer):

    class Meta:
        model = ssb_dwdate
        fields = ('d_datekey', 'd_date', 'd_dayofweek', 'd_month', 'd_month', 'd_year', 'd_yearmonthnum', 'd_yearmonth', 'd_daynuminweek', 'd_daynuminmonth', 'd_daynuminyear', 'd_monthnuminyear', 'd_weeknuminyear', 'd_sellingseason', 'd_lastdatinweekfl', 'd_lastdatinmonthfl', 'd_holidayfl' ,'d_weekdayfl')

class ssb_partSer(serializers.ModelSerializer):

    class Meta:
        model = ssb_part
        fields = ('p_partkey', 'p_name', 'p_mfgr', 'p_category', 'p_brand1', 'p_color', 'p_type', 'p_size', 'p_container')

class ssb_supSer(serializers.ModelSerializer):

    class Meta:
        model = ssb_supplier
        fields = ('s_suppkey', 's_name', 's_address', 's_city', 's_nation', 's_region', 's_phone')

class ssb_lineSer(serializers.ModelSerializer):

    class Meta:
        model = ssb_lineorder
        fields = ('lo_orderkey', 'lo_linenumber', 'lo_custkey', 'lo_partkey', 'lo_suppkey', 'lo_orderdate', 'lo_orderpriority', 'lo_shippriority', 'lo_quantity', 'lo_extendedprice', 'lo_ordertotalprice', 'lo_discount', 'lo_revenue', 'lo_supplycost', 'lo_tax', 'lo_commitdate', 'lo_shipmode', 'lo_pk')


class tpch_CustSer(serializers.ModelSerializer):

    class Meta:
        model = tpch_customer
        fields = ('c_custkey', 'c_name', 'c_address', 'c_nationkey', 'c_phone', 'c_acctbal', 'c_mktsegment', 'c_comment')


class tpch_NationSer(serializers.ModelSerializer):

    class Meta:
        model = tpch_nation
        fields = ('n_nationkey', 'n_name', 'n_regionkey', 'n_comment')

class tpch_lineitemSer(serializers.ModelSerializer):

    class Meta:
        model = tpch_lineitem
        fields = ('l_orderkey','l_partkey','l_suppkey','l_linenumber','l_quantity','l_extendedprice','l_discount','l_tax','l_returnflag','l_linestatus','l_shipdate','l_commitdate','l_receiptdate','l_shipinstruct','l_shipmode','l_comment','l_id')

class tpch_orderSer(serializers.ModelSerializer):

    class Meta:
        model = tpch_orders
        fields = ('o_orderkey','o_custkey','o_orderstatus','o_totalprice','o_orderdate','o_orderpriority','o_clerk','o_shippriority','o_comment')

class tpch_partSer(serializers.ModelSerializer):

    class Meta:
        model = tpch_part
        fields = ('p_partkey','p_name','p_mfgr','p_brand','p_type','p_size','p_container','p_retailprice','p_comment')

class tpch_partsuppSer(serializers.ModelSerializer):

    class Meta:
        model = tpch_partsupp
        fields = ('ps_partkey','ps_suppkey','ps_availqty','ps_supplycost','ps_comment','ps_id')

class tpch_regionSer(serializers.ModelSerializer):

    class Meta:
        model = tpch_region
        fields = ('r_regionkey','r_name','r_comment')

class tpch_supplierSer(serializers.ModelSerializer):

    class Meta:
        model = tpch_supplier
        fields = ('s_suppkey','s_name','s_address','s_nationkey','s_phone','s_acctbal','s_comment')