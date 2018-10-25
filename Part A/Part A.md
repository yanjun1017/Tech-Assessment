Part A.

Due to the extremely large data set, results are base on the dataset with a size of 1,000,000. 

Question: Consider only the 10 most common overall complaint types. For each borough, how many of each of 
those 10 types were there in 2017?

			     borough           complaint_type  count
			0          BRONX           HEAT/HOT WATER  36450
			1       BROOKLYN           HEAT/HOT WATER  33033
			2      MANHATTAN           HEAT/HOT WATER  23532
			3         QUEENS           HEAT/HOT WATER  14340
			4  STATEN ISLAND           HEAT/HOT WATER   1015
			0          BRONX      Noise - Residential  26911
			1       BROOKLYN      Noise - Residential  28855
			2      MANHATTAN      Noise - Residential  24631
			3         QUEENS      Noise - Residential  18509
			4  STATEN ISLAND      Noise - Residential   3052
			0          BRONX          Illegal Parking   6672
			1       BROOKLYN          Illegal Parking  24276
			2      MANHATTAN          Illegal Parking   8377
			3         QUEENS          Illegal Parking  20274
			4  STATEN ISLAND          Illegal Parking   3496
			0          BRONX         Blocked Driveway  10757
			1       BROOKLYN         Blocked Driveway  21509
			2      MANHATTAN         Blocked Driveway   1312
			3         QUEENS         Blocked Driveway  23513
			4  STATEN ISLAND         Blocked Driveway   1631
			0          BRONX         Street Condition   6190
			1       BROOKLYN         Street Condition  13515
			2      MANHATTAN         Street Condition   8239
			3         QUEENS         Street Condition  16509
			4  STATEN ISLAND         Street Condition   5839
			0          BRONX     UNSANITARY CONDITION  10803
			1       BROOKLYN     UNSANITARY CONDITION  11142
			2      MANHATTAN     UNSANITARY CONDITION   6369
			3         QUEENS     UNSANITARY CONDITION   4890
			4  STATEN ISLAND     UNSANITARY CONDITION    816
			0          BRONX             Water System   3748
			1       BROOKLYN             Water System   9207
			2      MANHATTAN             Water System   4574
			3         QUEENS             Water System   8536
			4  STATEN ISLAND             Water System   2390
			0          BRONX                    Noise   1344
			1       BROOKLYN                    Noise   6914
			2      MANHATTAN                    Noise  14087
			3         QUEENS                    Noise   5017
			4  STATEN ISLAND                    Noise    917
			0          BRONX            PAINT/PLASTER   9157
			1       BROOKLYN            PAINT/PLASTER   8925
			2      MANHATTAN            PAINT/PLASTER   5784
			3         QUEENS            PAINT/PLASTER   2644
			4  STATEN ISLAND            PAINT/PLASTER    459
			0          BRONX  Noise - Street/Sidewalk   4212
			1       BROOKLYN  Noise - Street/Sidewalk   7257
			2      MANHATTAN  Noise - Street/Sidewalk  10914
			3         QUEENS  Noise - Street/Sidewalk   2531
			4  STATEN ISLAND  Noise - Street/Sidewalk    305

Question: Consider only the 10 most common overall complaint types.  For the 10 most populous zip codes, 
how many of each of those 10 types were there in 2017?

	  incident_zip  complaint_type  count
	        11226  HEAT/HOT WATER   3982
	        11226  Noise - Residential   2292
	        11226  Illegal Parking    391
	        11226  Blocked Driveway    957
	        11226  Street Condition    276
	        11226  UNSANITARY CONDITION   1397
	        11226   Water System    143
	        11226          Noise    225
	        11226  PAINT/PLASTER   1336
	        11226  Noise - Street/Sidewalk    578

	  incident_zip  complaint_type  count
	        10467  HEAT/HOT WATER   3185
	        10467  Noise - Residential   2342
	        10467  Illegal Parking    496
	        10467  Blocked Driveway    897
	        10467  Street Condition    351
	        10467  UNSANITARY CONDITION    977
	        10467   Water System    235
	        10467          Noise    151
	        10467  PAINT/PLASTER    963
	        10467  Noise - Street/Sidewalk    194

	  incident_zip  complaint_type  count
	        10453  HEAT/HOT WATER   3258
	        10453  Noise - Residential   1643
	        10453  Illegal Parking    312
	        10453  Blocked Driveway    689
	        10453  Street Condition    240
	        10453  UNSANITARY CONDITION    891
	        10453   Water System    247
	        10453          Noise     55
	        10453  PAINT/PLASTER    935
	        10453  Noise - Street/Sidewalk    289

	  incident_zip  complaint_type  count
	        11385  HEAT/HOT WATER    696
	        11385  Noise - Residential   1034
	        11385  Illegal Parking   2001
	        11385  Blocked Driveway   1362
	        11385  Street Condition    681
	        11385  UNSANITARY CONDITION    279
	        11385   Water System    695
	        11385          Noise    209
	        11385  PAINT/PLASTER    148
	        11385  Noise - Street/Sidewalk    216

	  incident_zip  complaint_type  count
	        10468  HEAT/HOT WATER   2849
	        10468  Noise - Residential   2799
	        10468  Illegal Parking    378
	        10468  Blocked Driveway    417
	        10468  Street Condition    206
	        10468  UNSANITARY CONDITION    660
	        10468   Water System    197
	        10468          Noise    101
	        10468  PAINT/PLASTER    737
	        10468  Noise - Street/Sidewalk    412
	  
	  incident_zip  complaint_type  count
	        10458  HEAT/HOT WATER   3517
	        10458  Noise - Residential   1896
	        10458  Illegal Parking    230
	        10458  Blocked Driveway    398
	        10458  Street Condition    249
	        10458  UNSANITARY CONDITION    910
	        10458   Water System    135
	        10458          Noise     63
	        10458  PAINT/PLASTER    822 
	        10458  Noise - Street/Sidewalk    298
	  
	  incident_zip  complaint_type  count
	        10452  HEAT/HOT WATER   2763
	        10452  Noise - Residential   1867
	        10452  Illegal Parking    236
	        10452  Blocked Driveway    493
	        10452  Street Condition    199
	        10452  UNSANITARY CONDITION    859
	        10452   Water System    217
	        10452          Noise     72
	        10452  PAINT/PLASTER    731
	        10452  Noise - Street/Sidewalk    383

	  incident_zip  complaint_type  count
	        11207  HEAT/HOT WATER   1166
	        11207  Noise - Residential   1192
	        11207  Illegal Parking    646
	        11207  Blocked Driveway    844
	        11207  Street Condition    603
	        11207  UNSANITARY CONDITION    603
	        11207   Water System    302
	        11207          Noise     96
	        11207  PAINT/PLASTER    486
	        11207  Noise - Street/Sidewalk    175

	  incident_zip  complaint_type  count
	        10031  HEAT/HOT WATER   2363
	        10031  Noise - Residential   2082
	        10031  Illegal Parking    185
	        10031  Blocked Driveway     37
	        10031  Street Condition    117
	        10031  UNSANITARY CONDITION    580
	        10031   Water System    285
	        10031          Noise    161
	        10031  PAINT/PLASTER    732
	        10031  Noise - Street/Sidewalk   1410
	  
	  incident_zip  complaint_type  count
	        11208  HEAT/HOT WATER   1033
	        11208  Noise - Residential   1118
	        11208  Illegal Parking    895
	        11208  Blocked Driveway   1156
	        11208  Street Condition    458
	        11208  UNSANITARY CONDITION    588
	        11208   Water System    210
	        11208          Noise     73
	        11208  PAINT/PLASTER    418  
	        11208  Noise - Street/Sidewalk    242

Question: Considering all complaint types. Which boroughs are the biggest "complainers" relative 
to the size of the population in 2017? Meaning, calculate a complaint-index that adjusts for population 
of the borough.

	Top:

		borough        count  2010 Census Population     index
		STATEN ISLAND    645                468730.0  1.211753

	All:

		borough        count  2010 Census Population     index                                       
		STATEN ISLAND    645                468730.0  1.211753
		QUEENS          2693               2348742.0  1.009667
		BROOKLYN        2934               2603292.0  0.992463
		BRONX           1550               1382480.0  0.987302
		MANHATTAN       1757               1631991.0  0.948050



