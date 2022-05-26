def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9995
   if obj[3] == 'Sell':
      # Feature: SMA2, Instances: 76, Entropy: 0.9754
      if obj[5] == 'Buy':
         # Feature: MACD, Instances: 40, Entropy: 1.0
         if obj[2] == 'Sell':
            # Feature: Closing, Instances: 37, Entropy: 0.9953
            if obj[0]<=74.781998:
               # Feature: SMA1, Instances: 29, Entropy: 0.9991
               if obj[4] == 'Buy':
                  # Feature: RSI, Instances: 20, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: RSI, Instances: 9, Entropy: 0.9911
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]>74.781998:
               # Feature: SMA1, Instances: 8, Entropy: 0.9544
               if obj[4] == 'Buy':
                  # Feature: RSI, Instances: 7, Entropy: 0.9852
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[2] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[5] == 'Sell':
         # Feature: SMA1, Instances: 36, Entropy: 0.888
         if obj[4] == 'Sell':
            # Feature: MACD, Instances: 21, Entropy: 0.7919
            if obj[2] == 'Buy':
               # Feature: Closing, Instances: 17, Entropy: 0.874
               if obj[0]<=74.781998:
                  # Feature: RSI, Instances: 16, Entropy: 0.896
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]>74.781998:
                  return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Sell':
               return 'No'
            else:
               return 'No'
         elif obj[4] == 'Buy':
            # Feature: Closing, Instances: 15, Entropy: 0.971
            if obj[0]<=74.781998:
               # Feature: RSI, Instances: 12, Entropy: 0.9183
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 11, Entropy: 0.9457
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[1] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            elif obj[0]>74.781998:
               # Feature: MACD, Instances: 3, Entropy: 0.9183
               if obj[2] == 'Sell':
                  # Feature: RSI, Instances: 2, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'No'
      else:
         return 'No'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 34, Entropy: 0.6723
      if obj[1] == 'Hold':
         # Feature: Closing, Instances: 23, Entropy: 0.8281
         if obj[0]<=74.781998:
            # Feature: MACD, Instances: 18, Entropy: 0.9183
            if obj[2] == 'Buy':
               # Feature: SMA1, Instances: 13, Entropy: 0.9957
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 10, Entropy: 0.8813
                  if obj[5] == 'Buy':
                     return 'Yes'
                  elif obj[5] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[0]>74.781998:
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
