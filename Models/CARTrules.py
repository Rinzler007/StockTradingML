def findDecision(obj):
   # Feature: BB, Instances: 2863, Gini: 0.3935
   if obj[3] == 'Sell':
      # Feature: RSI, Instances: 1712, Gini: 0.4557
      if obj[1] == 'Hold':
         # Feature: Closing, Instances: 1632, Gini: 0.4678
         if obj[0]<=75.961998:
            # Feature: SMA2, Instances: 1340, Gini: 0.4566
            if obj[5] == 'Sell':
               # Feature: SMA1, Instances: 766, Gini: 0.4149
               if obj[4] == 'Sell':
                  # Feature: MACD, Instances: 454, Gini: 0.4795
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: MACD, Instances: 312, Gini: 0.3185
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: SMA1, Instances: 574, Gini: 0.4851
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 404, Gini: 0.488
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: MACD, Instances: 170, Gini: 0.4775
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[0]>75.961998:
            # Feature: SMA2, Instances: 292, Gini: 0.4916
            if obj[5] == 'Buy':
               # Feature: MACD, Instances: 164, Gini: 0.484
               if obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 150, Gini: 0.491
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 14, Gini: 0.3673
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: MACD, Instances: 128, Gini: 0.4769
               if obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 73, Gini: 0.4898
                  if obj[4] == 'Sell':
                     return 'Yes'
                  elif obj[4] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 55, Gini: 0.4405
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'Yes'
      elif obj[1] == 'Buy':
         # Feature: SMA2, Instances: 76, Gini: 0.0258
         if obj[5] == 'Sell':
            # Feature: Closing, Instances: 49, Gini: 0.0398
            if obj[0]<=75.961998:
               # Feature: SMA1, Instances: 39, Gini: 0.0498
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 34, Gini: 0.0571
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            elif obj[0]>75.961998:
               return 'No'
            else:
               return 'No'
         elif obj[5] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[1] == 'Sell':
         # Feature: SMA1, Instances: 4, Gini: 0.25
         if obj[4] == 'Buy':
            # Feature: Closing, Instances: 2, Gini: 0.0
            if obj[0]<=75.961998:
               return 'No'
            elif obj[0]>75.961998:
               return 'Yes'
            else:
               return 'Yes'
         elif obj[4] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 1019, Gini: 0.2831
      if obj[1] == 'Hold':
         # Feature: SMA1, Instances: 637, Gini: 0.3601
         if obj[4] == 'Buy':
            # Feature: SMA2, Instances: 417, Gini: 0.2881
            if obj[5] == 'Buy':
               # Feature: Closing, Instances: 395, Gini: 0.2763
               if obj[0]<=75.961998:
                  # Feature: MACD, Instances: 270, Gini: 0.3061
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[0]>75.961998:
                  # Feature: MACD, Instances: 125, Gini: 0.2101
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: Closing, Instances: 22, Gini: 0.3818
               if obj[0]<=75.961998:
                  # Feature: MACD, Instances: 20, Gini: 0.42
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]>75.961998:
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[4] == 'Sell':
            # Feature: SMA2, Instances: 220, Gini: 0.4531
            if obj[5] == 'Buy':
               # Feature: MACD, Instances: 157, Gini: 0.4655
               if obj[2] == 'Buy':
                  # Feature: Closing, Instances: 155, Gini: 0.4648
                  if obj[0]<=75.961998:
                     return 'Yes'
                  elif obj[0]>75.961998:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: Closing, Instances: 2, Gini: 0.5
                  if obj[0]<=75.961998:
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: Closing, Instances: 63, Gini: 0.413
               if obj[0]<=75.961998:
                  # Feature: MACD, Instances: 57, Gini: 0.4038
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[0]>75.961998:
                  # Feature: MACD, Instances: 6, Gini: 0.5
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[1] == 'Sell':
         # Feature: SMA1, Instances: 382, Gini: 0.1252
         if obj[4] == 'Buy':
            # Feature: SMA2, Instances: 287, Gini: 0.0561
            if obj[5] == 'Buy':
               # Feature: Closing, Instances: 276, Gini: 0.0425
               if obj[0]<=75.961998:
                  # Feature: MACD, Instances: 176, Gini: 0.0335
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[0]>75.961998:
                  # Feature: MACD, Instances: 100, Gini: 0.0582
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: Closing, Instances: 11, Gini: 0.2182
               if obj[0]>75.961998:
                  return 'Yes'
               elif obj[0]<=75.961998:
                  # Feature: MACD, Instances: 5, Gini: 0.48
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[4] == 'Sell':
            # Feature: Closing, Instances: 95, Gini: 0.3113
            if obj[0]<=75.961998:
               # Feature: SMA2, Instances: 78, Gini: 0.3443
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 62, Gini: 0.3122
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 16, Gini: 0.4688
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]>75.961998:
               # Feature: SMA2, Instances: 17, Gini: 0.1029
               if obj[5] == 'Buy':
                  return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 8, Gini: 0.2188
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      # Feature: MACD, Instances: 132, Gini: 0.1548
      if obj[2] == 'Sell':
         # Feature: RSI, Instances: 128, Gini: 0.1401
         if obj[1] == 'Hold':
            # Feature: SMA1, Instances: 66, Gini: 0.2084
            if obj[4] == 'Sell':
               # Feature: Closing, Instances: 57, Gini: 0.2399
               if obj[0]<=75.961998:
                  # Feature: SMA2, Instances: 55, Gini: 0.247
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]>75.961998:
                  return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Buy':
               return 'No'
            else:
               return 'No'
         elif obj[1] == 'Buy':
            # Feature: SMA1, Instances: 62, Gini: 0.0619
            if obj[4] == 'Sell':
               # Feature: SMA2, Instances: 49, Gini: 0.0781
               if obj[5] == 'Sell':
                  # Feature: Closing, Instances: 46, Gini: 0.0831
                  if obj[0]<=75.961998:
                     return 'No'
                  elif obj[0]>75.961998:
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Buy':
               return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[2] == 'Buy':
         # Feature: Closing, Instances: 4, Gini: 0.5
         if obj[0]<=75.961998:
            # Feature: RSI, Instances: 4, Gini: 0.5
            if obj[1] == 'Hold':
               # Feature: SMA1, Instances: 4, Gini: 0.5
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 4, Gini: 0.5
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      else:
         return 'No'
   else:
      return 'No'
