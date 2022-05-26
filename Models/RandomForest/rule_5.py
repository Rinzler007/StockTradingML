def findDecision(obj):
   # Feature: RSI, Instances: 115, Entropy: 0.9973
   if obj[1] == 'Hold':
      # Feature: Closing, Instances: 95, Entropy: 0.998
      if obj[0]>33.273998:
         # Feature: BB, Instances: 63, Entropy: 0.9334
         if obj[3] == 'Sell':
            # Feature: SMA1, Instances: 46, Entropy: 0.8865
            if obj[4] == 'Sell':
               # Feature: SMA2, Instances: 25, Entropy: 0.9427
               if obj[5] == 'Sell':
                  # Feature: MACD, Instances: 19, Entropy: 0.9819
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Buy':
                  # Feature: MACD, Instances: 6, Entropy: 0.65
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Buy':
               # Feature: MACD, Instances: 21, Entropy: 0.7919
               if obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 18, Entropy: 0.8524
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[3] == 'Hold':
            # Feature: SMA1, Instances: 16, Entropy: 1.0
            if obj[4] == 'Buy':
               # Feature: SMA2, Instances: 9, Entropy: 0.5033
               if obj[5] == 'Buy':
                  return 'Yes'
               elif obj[5] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               return 'No'
            else:
               return 'No'
         elif obj[3] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[0]<=33.273998:
         # Feature: BB, Instances: 32, Entropy: 0.8571
         if obj[3] == 'Sell':
            # Feature: SMA2, Instances: 21, Entropy: 0.9587
            if obj[5] == 'Buy':
               # Feature: MACD, Instances: 15, Entropy: 0.8366
               if obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 10, Entropy: 0.971
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Buy':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: SMA1, Instances: 6, Entropy: 0.9183
               if obj[4] == 'Sell':
                  # Feature: MACD, Instances: 4, Entropy: 1.0
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[3] == 'Hold':
            return 'Yes'
         elif obj[3] == 'Buy':
            return 'No'
         else:
            return 'No'
      else:
         return 'Yes'
   elif obj[1] == 'Sell':
      return 'Yes'
   elif obj[1] == 'Buy':
      return 'No'
   else:
      return 'No'
