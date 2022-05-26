def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9842
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 73, Entropy: 0.9693
      if obj[0]<=68.905998:
         # Feature: SMA1, Instances: 58, Entropy: 0.9124
         if obj[4] == 'Sell':
            # Feature: SMA2, Instances: 30, Entropy: 1.0
            if obj[5] == 'Sell':
               # Feature: MACD, Instances: 21, Entropy: 0.9852
               if obj[2] == 'Buy':
                  # Feature: RSI, Instances: 17, Entropy: 0.9975
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: RSI, Instances: 4, Entropy: 0.8113
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Buy':
               # Feature: RSI, Instances: 9, Entropy: 0.9183
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 8, Entropy: 0.9544
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
            else:
               return 'No'
         elif obj[4] == 'Buy':
            # Feature: MACD, Instances: 28, Entropy: 0.5917
            if obj[2] == 'Sell':
               # Feature: SMA2, Instances: 21, Entropy: 0.7025
               if obj[5] == 'Sell':
                  # Feature: RSI, Instances: 11, Entropy: 0.4395
                  if obj[1] == 'Hold':
                     return 'No'
                  elif obj[1] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Buy':
                  # Feature: RSI, Instances: 10, Entropy: 0.8813
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Buy':
               return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[0]>68.905998:
         # Feature: MACD, Instances: 15, Entropy: 0.9183
         if obj[2] == 'Sell':
            # Feature: SMA1, Instances: 11, Entropy: 0.9457
            if obj[4] == 'Buy':
               # Feature: SMA2, Instances: 10, Entropy: 0.8813
               if obj[5] == 'Buy':
                  # Feature: RSI, Instances: 8, Entropy: 0.8113
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: RSI, Instances: 2, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               return 'No'
            else:
               return 'No'
         elif obj[2] == 'Buy':
            # Feature: SMA1, Instances: 4, Entropy: 0.8113
            if obj[4] == 'Sell':
               return 'Yes'
            elif obj[4] == 'Buy':
               # Feature: RSI, Instances: 2, Entropy: 1.0
               if obj[1] == 'Hold':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: Closing, Instances: 40, Entropy: 0.3843
      if obj[0]<=68.905998:
         # Feature: RSI, Instances: 25, Entropy: 0.5294
         if obj[1] == 'Hold':
            # Feature: SMA2, Instances: 18, Entropy: 0.65
            if obj[5] == 'Buy':
               # Feature: MACD, Instances: 14, Entropy: 0.7496
               if obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 11, Entropy: 0.8454
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[1] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      elif obj[0]>68.905998:
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
