def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9934
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 66, Entropy: 0.9327
      if obj[0]<=71.594002:
         # Feature: MACD, Instances: 50, Entropy: 0.795
         if obj[2] == 'Sell':
            # Feature: SMA1, Instances: 27, Entropy: 0.8767
            if obj[4] == 'Buy':
               # Feature: SMA2, Instances: 19, Entropy: 0.8315
               if obj[5] == 'Buy':
                  # Feature: RSI, Instances: 14, Entropy: 0.7496
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: RSI, Instances: 5, Entropy: 0.971
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: SMA2, Instances: 8, Entropy: 0.9544
               if obj[5] == 'Buy':
                  # Feature: RSI, Instances: 5, Entropy: 0.971
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: RSI, Instances: 3, Entropy: 0.9183
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[2] == 'Buy':
            # Feature: SMA1, Instances: 23, Entropy: 0.6666
            if obj[4] == 'Sell':
               # Feature: SMA2, Instances: 21, Entropy: 0.7025
               if obj[5] == 'Sell':
                  # Feature: RSI, Instances: 16, Entropy: 0.6962
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Buy':
                  # Feature: RSI, Instances: 5, Entropy: 0.7219
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Buy':
               return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[0]>71.594002:
         # Feature: RSI, Instances: 16, Entropy: 0.896
         if obj[1] == 'Hold':
            # Feature: MACD, Instances: 15, Entropy: 0.8366
            if obj[2] == 'Sell':
               # Feature: SMA2, Instances: 11, Entropy: 0.684
               if obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 9, Entropy: 0.7642
                  if obj[4] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[2] == 'Buy':
               # Feature: SMA1, Instances: 4, Entropy: 1.0
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[1] == 'Buy':
            return 'No'
         else:
            return 'No'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 45, Entropy: 0.5033
      if obj[1] == 'Hold':
         # Feature: Closing, Instances: 28, Entropy: 0.6769
         if obj[0]<=71.594002:
            # Feature: SMA1, Instances: 20, Entropy: 0.8113
            if obj[4] == 'Sell':
               # Feature: SMA2, Instances: 10, Entropy: 0.7219
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 8, Entropy: 0.8113
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[4] == 'Buy':
               # Feature: SMA2, Instances: 10, Entropy: 0.8813
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 9, Entropy: 0.7642
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[0]>71.594002:
            return 'Yes'
         else:
            return 'Yes'
      elif obj[1] == 'Sell':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
