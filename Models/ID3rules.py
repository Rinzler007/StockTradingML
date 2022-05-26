def findDecision(obj):
   # Feature: BB, Instances: 2863, Entropy: 0.9989
   if obj[3] == 'Sell':
      # Feature: RSI, Instances: 1712, Entropy: 0.954
      if obj[1] == 'Hold':
         # Feature: Closing, Instances: 1632, Entropy: 0.965
         if obj[0] == '<=75.961998':
            # Feature: SMA2, Instances: 1340, Entropy: 0.9431
            if obj[5] == 'Sell':
               # Feature: SMA1, Instances: 766, Entropy: 0.9042
               if obj[4] == 'Sell':
                  # Feature: MACD, Instances: 454, Entropy: 0.9727
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: MACD, Instances: 312, Entropy: 0.7194
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: SMA1, Instances: 574, Entropy: 0.9789
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 404, Entropy: 0.9829
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: MACD, Instances: 170, Entropy: 0.9674
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
         elif obj[0] == '>75.961998':
            # Feature: SMA2, Instances: 292, Entropy: 0.9978
            if obj[5] == 'Buy':
               # Feature: MACD, Instances: 164, Entropy: 0.9818
               if obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 150, Entropy: 0.9871
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 14, Entropy: 0.8631
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: MACD, Instances: 128, Entropy: 0.9956
               if obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 73, Entropy: 0.9934
                  if obj[4] == 'Sell':
                     return 'No'
                  elif obj[4] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 55, Entropy: 0.9299
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
         # Feature: SMA2, Instances: 76, Entropy: 0.1011
         if obj[5] == 'Sell':
            # Feature: Closing, Instances: 49, Entropy: 0.1437
            if obj[0] == '<=75.961998':
               # Feature: SMA1, Instances: 39, Entropy: 0.172
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 34, Entropy: 0.1914
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            elif obj[0] == '>75.961998':
               return 'No'
            else:
               return 'No'
         elif obj[5] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[1] == 'Sell':
         # Feature: SMA1, Instances: 4, Entropy: 0.8113
         if obj[4] == 'Sell':
            return 'Yes'
         elif obj[4] == 'Buy':
            # Feature: Closing, Instances: 2, Entropy: 1.0
            if obj[0] == '>75.961998':
               return 'Yes'
            elif obj[0] == '<=75.961998':
               return 'No'
            else:
               return 'No'
         else:
            return 'No'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 1019, Entropy: 0.6835
      if obj[1] == 'Hold':
         # Feature: SMA1, Instances: 637, Entropy: 0.8056
         if obj[4] == 'Buy':
            # Feature: SMA2, Instances: 417, Entropy: 0.7053
            if obj[5] == 'Buy':
               # Feature: Closing, Instances: 395, Entropy: 0.651
               if obj[0] == '<=75.961998':
                  # Feature: MACD, Instances: 270, Entropy: 0.6991
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[0] == '>75.961998':
                  # Feature: MACD, Instances: 125, Entropy: 0.5294
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: Closing, Instances: 22, Entropy: 0.9457
               if obj[0] == '<=75.961998':
                  # Feature: MACD, Instances: 20, Entropy: 0.8813
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0] == '>75.961998':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[4] == 'Sell':
            # Feature: SMA2, Instances: 220, Entropy: 0.9341
            if obj[5] == 'Buy':
               # Feature: MACD, Instances: 157, Entropy: 0.9502
               if obj[2] == 'Buy':
                  # Feature: Closing, Instances: 155, Entropy: 0.9489
                  if obj[0] == '<=75.961998':
                     return 'Yes'
                  elif obj[0] == '>75.961998':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: Closing, Instances: 2, Entropy: 1.0
                  if obj[0] == '<=75.961998':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Sell':
               # Feature: Closing, Instances: 63, Entropy: 0.8832
               if obj[0] == '<=75.961998':
                  # Feature: MACD, Instances: 57, Entropy: 0.8564
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[0] == '>75.961998':
                  # Feature: MACD, Instances: 6, Entropy: 1.0
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[1] == 'Sell':
         # Feature: SMA1, Instances: 382, Entropy: 0.3781
         if obj[4] == 'Buy':
            # Feature: SMA2, Instances: 287, Entropy: 0.2012
            if obj[5] == 'Buy':
               # Feature: Closing, Instances: 276, Entropy: 0.1511
               if obj[0] == '<=75.961998':
                  # Feature: MACD, Instances: 176, Entropy: 0.1245
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[0] == '>75.961998':
                  # Feature: MACD, Instances: 100, Entropy: 0.1944
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: Closing, Instances: 11, Entropy: 0.8454
               if obj[0] == '>75.961998':
                  return 'Yes'
               elif obj[0] == '<=75.961998':
                  # Feature: MACD, Instances: 5, Entropy: 0.971
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[4] == 'Sell':
            # Feature: Closing, Instances: 95, Entropy: 0.7219
            if obj[0] == '<=75.961998':
               # Feature: SMA2, Instances: 78, Entropy: 0.7793
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 62, Entropy: 0.7088
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 16, Entropy: 0.9544
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[0] == '>75.961998':
               # Feature: SMA2, Instances: 17, Entropy: 0.3228
               if obj[5] == 'Buy':
                  return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 8, Entropy: 0.5436
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
      # Feature: RSI, Instances: 132, Entropy: 0.4395
      if obj[1] == 'Hold':
         # Feature: MACD, Instances: 70, Entropy: 0.5917
         if obj[2] == 'Sell':
            # Feature: SMA1, Instances: 66, Entropy: 0.5328
            if obj[4] == 'Sell':
               # Feature: Closing, Instances: 57, Entropy: 0.5852
               if obj[0] == '<=75.961998':
                  # Feature: SMA2, Instances: 55, Entropy: 0.5983
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0] == '>75.961998':
                  return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Buy':
               return 'No'
            else:
               return 'No'
         elif obj[2] == 'Buy':
            # Feature: Closing, Instances: 4, Entropy: 1.0
            if obj[0] == '<=75.961998':
               # Feature: SMA1, Instances: 4, Entropy: 1.0
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 4, Entropy: 1.0
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
      elif obj[1] == 'Buy':
         # Feature: SMA1, Instances: 62, Entropy: 0.2056
         if obj[4] == 'Sell':
            # Feature: SMA2, Instances: 49, Entropy: 0.246
            if obj[5] == 'Sell':
               # Feature: Closing, Instances: 46, Entropy: 0.258
               if obj[0] == '<=75.961998':
                  # Feature: MACD, Instances: 45, Entropy: 0.2623
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0] == '>75.961998':
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
   else:
      return 'No'
